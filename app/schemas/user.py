from pydantic import BaseModel, EmailStr
from app.models.enums import UserType, PersonType, GenderType

class UserCreateSchema(BaseModel):
    user_type: UserType
    person_type: PersonType
    full_name: str
    email: EmailStr
    cell_phone: str
    gender: GenderType
    password: str

class UserResponseSchema(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    user_type: UserType
    person_type: PersonType
