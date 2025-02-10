from fastapi import APIRouter, status, Body, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
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

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return '1'
    # Executa a consulta SQL manualmente
    result = db.execute(text("SELECT * FROM users;"))
    users = result.fetchall()  # Obtém todos os resultados

    # Converte os resultados em uma lista de dicionários
    users_list = [dict(row) for row in users]
    
    return users_list