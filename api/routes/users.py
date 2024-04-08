from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore

from api.deps import get_db
from api.schemas.users import UserCreate, UserOutPut
from core.utils import get_current_active_user, get_current_active_superuser
from api.crud.users import get_user, get_user_by_username, create_user
from core.config import settings

router = APIRouter(
    prefix='/users'
)


@router.post('/', dependencies=[Depends(get_current_active_superuser)])
async def create_new_user(user: UserCreate, session: Session = Depends(get_db)):
    db_user = get_user_by_username(session=session, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(session, user)


@router.get('/{user_id}', response_model=UserOutPut, dependencies=[Depends(get_current_active_superuser)])
async def read_user(user_id: int, session: Session = Depends(get_db)):
    db_user = get_user(session=session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.post('/signup', response_model=UserOutPut)
async def register_user(user_in: UserCreate, session: Session = Depends(get_db)):

    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )

    user = get_user_by_username(session=session, username=user_in.username)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )

    user = create_user(session, user_in)

    user_response = UserOutPut(
        id=user.id,
        username=user.username,
        email=user.email,
    )

    return user_response
