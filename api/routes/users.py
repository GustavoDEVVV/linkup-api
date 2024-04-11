from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.deps import get_current_active_superuser, CurrentUser, get_current_active_user
from api.schemas.users import UserCreate, UserOutPut, UserUpdateMe
from api.crud.users import get_user_by_username, create_user, select_users
from api.models.users import UserModel

from core.config import settings
from core.database import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', dependencies=[Depends(get_current_active_superuser)])
async def create_new_user(user: UserCreate, session: Session = Depends(get_db)):
    db_user = get_user_by_username(session=session, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(session, user)


@router.get('/{username}', dependencies=[Depends(get_current_active_user)])
async def read_user(username: str, session: Session = Depends(get_db)):
    db_user = get_user_by_username(session=session, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.get('/', dependencies=[Depends(get_current_active_superuser)])
async def read_user(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
    try:
        user_posts = []
        users = select_users(session, skip=skip, limit=limit)
        for user in users:
            user_dict = user.__dict__
            user_dict['posts'] = [post.__dict__ for post in user.posts]
            user_dict.pop('id')
            user_dict.pop('email')
            user_dict.pop('hashed_password')

            user_dict.pop('is_superuser')
            user_dict.pop('disabled')

            user_posts.append(user_dict)

            for post in user_dict['posts']:
                post.pop('id')
                post.pop('owner_username')

            return user_posts
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


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


@router.put('/{username}', dependencies=[Depends(get_current_active_user)])
async def update_me(data: UserUpdateMe,
                    username: str,
                    current_user: CurrentUser,
                    session: Session = Depends(get_db)):

    if username != current_user.username:
        raise HTTPException(status_code=404, detail='Forbidden')

    db_user = session.query(UserModel).filter(
        UserModel.username == username).first()

    if data.email != db_user.email:
        existing_user_email = session.query(UserModel).filter(
            UserModel.email == data.email).first()
        if existing_user_email:
            raise HTTPException(status_code=400, detail='Email already in use')

    if data.username != db_user.username:
        existing_user_username = session.query(UserModel).filter(
            UserModel.username == data.username).first()
        if existing_user_username:
            raise HTTPException(
                status_code=400, detail='Username already in use')

    db_user.username = data.username
    db_user.email = data.email
    session.commit()
    session.refresh(db_user)

    return data
