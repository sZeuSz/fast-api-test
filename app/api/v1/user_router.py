from fastapi import APIRouter, status, Body, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreateSchema, UserResponseSchema
from app.repositories.user import UserRepository
from app.services.user import UserService

router = APIRouter()

@router.post("/user", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    create_user_request: UserCreateSchema = Body(...),
    db: Session = Depends(get_db)
):
    print(f'''create_user_request: {create_user_request}''')
    user_repository = UserRepository(db)
    print(f'''user_repository: {user_repository}''')
    user_service = UserService(user_repository)
    return user_service.create_user(create_user_request)
