from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schemas.reactions import ReactionCreate
from api.crud.posts import get_post_by_id
from api.crud.users import get_user_by_username
from api.deps import get_current_active_user, get_db, CurrentUser
from api.crud.reactions import create_like, get_likes_by_post_id, delete_like

router = APIRouter(prefix='/posts/{post_id}/reactions', tags=['reactions'])


@router.post('/', dependencies=[Depends(get_current_active_user)])
async def post_like(
    post_id: str,
    data: ReactionCreate,
    current_user: CurrentUser,
    session: Session = Depends(get_db),
):
    try:
        user_id = current_user.id
        username = current_user.username

        post = get_post_by_id(session=session, post_id=post_id)
        user = get_user_by_username(session=session, username=username)

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        created_like = create_like(
            session=session,
            post_id=post_id,
            user_id=user_id,
            reaction=data.reaction
        )

        return created_like

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/')
async def get_likes_for_post(post_id: str, session: Session = Depends(get_db)):
    try:
        post = get_post_by_id(session=session, post_id=post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        likes = get_likes_by_post_id(session=session, post_id=post_id)
        return likes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/', dependencies=[Depends(get_current_active_user)])
async def unlike_post(
    post_id: str,
    current_user: CurrentUser,
    session: Session = Depends(get_db),
):
    try:
        user_id = current_user.id
        username = current_user.username

        post = get_post_by_id(session=session, post_id=post_id)
        user = get_user_by_username(session=session, username=username)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        result = delete_like(
            session=session,
            post_id=post_id,
            user_id=user_id
        )

        if result:
            return {"message": "Like deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Like not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
