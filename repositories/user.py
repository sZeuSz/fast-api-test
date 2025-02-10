from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreateSchema

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email_or_phone(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_data: UserCreateSchema, hashed_password: str):
        new_user = User(
            user_type=user_data.user_type,
            person_type=user_data.person_type,
            full_name=user_data.full_name,
            email=user_data.email,
            cell_phone=user_data.cell_phone,
            gender=user_data.gender,
            password=hashed_password
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
