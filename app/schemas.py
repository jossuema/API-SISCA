from pydantic import BaseModel, EmailStr, HttpUrl
from enum import Enum
from typing import Optional

class UserRoleEnum(str, Enum):
    teacher = "teacher"
    admin = "admin"

# Schema para la creación de usuarios
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    lastname: str
    role: UserRoleEnum
    img_url: Optional[HttpUrl]

# Schema para la respuesta de datos del usuario
class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    name: str
    lastname: str
    role: UserRoleEnum
    img_url: Optional[HttpUrl]

    class Config:
        orm_mode = True

# Schema para login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema para el token
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

# Schema para la solicitud de refresh token
class TokenRefreshRequest(BaseModel):
    refresh_token: str