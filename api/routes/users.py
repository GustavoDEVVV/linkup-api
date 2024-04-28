from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.deps import get_current_active_superuser, CurrentUser, get_current_active_user
from api.crud.users import get_user_by_username, select_users, delete_user, create_super_user, update_user
from api.schemas.users import UserUpdateMe, UserCreateSuperUser
from api.models.users import UserModel

from core.database import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', dependencies=[Depends(get_current_active_superuser)])
async def create_new_user(user: UserCreateSuperUser, session: Session = Depends(get_db)):
    db_user = get_user_by_username(session=session, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_super_user(session, user)


@router.get('/{username}', dependencies=[Depends(get_current_active_user)])
async def read_user(username: str, session: Session = Depends(get_db)):
    db_user = get_user_by_username(session=session, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.get('/', dependencies=[Depends(get_current_active_superuser)])
async def read_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)):
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


@router.put('/{username}', dependencies=[Depends(get_current_active_user)])
async def update_me(data: UserUpdateMe,
                    username: str,
                    current_user: CurrentUser,
                    session: Session = Depends(get_db)):

    if username != current_user.username:
        raise HTTPException(status_code=404, detail='Forbidden')

    updated_user = update_user(session=session, data=data, username=username)
    # db_user = session.query(UserModel).filter(
    #     UserModel.username == username).first()

    # if data.email != db_user.email:
    #     existing_user_email = session.query(UserModel).filter(
    #         UserModel.email == data.email).first()
    #     if existing_user_email:
    #         raise HTTPException(status_code=400, detail='Email already in use')

    # if data.username != db_user.username:
    #     existing_user_username = session.query(UserModel).filter(
    #         UserModel.username == data.username).first()
    #     if existing_user_username:
    #         raise HTTPException(
    #             status_code=400, detail='Username already in use')

    # db_user.username = data.username
    # db_user.email = data.email
    # session.commit()
    # session.refresh(db_user)

    return updated_user


@router.delete('/{username}', dependencies=[Depends(get_current_active_superuser)])
async def remove_user(username: str, session: Session = Depends(get_db)):
    db_user = get_user_by_username(session=session, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    delete_user(session=session, user=db_user)
    return {"message": f"User {username} deleted."}
