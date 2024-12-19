from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import UserCreate, UserResponse, Token, TokenRefreshRequest
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import create_user, get_user_by_email, verify_password, create_access_token, create_refresh_token
import os

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# Endpoint de registro
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(db, user.email, user.name, user.lastname, user.password, user.role, user.img_url)
    return new_user

# Endpoint de login
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.user_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.user_email, "role": user.user_role.value})
    refresh_token = create_refresh_token({"sub": user.user_email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

# Endpoint para renovar el access token
@router.post("/refresh-token", response_model=Token)
def refresh_token(request: TokenRefreshRequest, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(request.refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user_by_email(db, email)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        new_access_token = create_access_token({"sub": user.user_email, "role": user.user_role.value})
        return {"access_token": new_access_token, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Endpoint para obtener datos del usuario autenticado
@router.get("/me", response_model=UserResponse)
def get_me(token: str = Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        user = get_user_by_email(db, email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "user_id": user.user_id,
            "email": user.user_email,
            "name": user.user_name,
            "lastname": user.user_lastname,
            "role": user.user_role.value,
            "img_url": user.user_img
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")