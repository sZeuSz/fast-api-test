from passlib.context import CryptContext
from app.schemas.user import UserCreateSchema, UserResponseSchema
from app.repositories.user import UserRepository
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(
        self,
        user_data: UserCreateSchema
    ) -> UserResponseSchema:
        existing_user = self.user_repository.get_by_email_or_phone(user_data.email)
        print(f'''existing_user: {existing_user}''')
        if existing_user:
            raise HTTPException(status_code=400, detail="Email ou celular já cadastrados")

        hashed_password = pwd_context.hash(user_data.password)

        new_user = self.user_repository.create(user_data, hashed_password)

        return UserResponseSchema(
            id=new_user.id,
            full_name=new_user.full_name,
            email=new_user.email,
            user_type=new_user.user_type,
            person_type=new_user.person_type,
        )
