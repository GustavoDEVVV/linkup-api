from sqlalchemy.orm import Session
from api.models.reactions import ReactionModel
from fastapi import HTTPException

from api.models.users import UserModel
from api.models.posts import PostModel

from api.schemas.reactions import ReactionUpdate


def create_like(session: Session, post_id: str, user_id: str, reaction: str):
    db_like = ReactionModel(
        postId=post_id,
        userId=user_id,
        reaction=reaction
    )

    session.add(db_like)
    session.commit()
    session.refresh(db_like)

    return db_like


def get_likes_by_post_id(session: Session, post_id: str):
    return session.query(ReactionModel).filter(ReactionModel.postId == post_id).all()


def delete_like(session: Session, post_id: str, user_id: str):
    like = (
        session.query(ReactionModel)
        .filter(ReactionModel.postId == post_id, ReactionModel.userId == user_id)
        .first()
    )
    if like:
        session.delete(like)
        session.commit()
        return {"message": "Like deleted successfully"}
    else:
        return {"message": "Like not found"}


def get_users_who_liked_post(session: Session, post_id: str):
    return (
        session.query(UserModel)
        .join(ReactionModel, UserModel.id == ReactionModel.userId)
        .filter(ReactionModel.postId == post_id)
        .all()
    )


def update_reaction(session: Session, post_id: str, user_id: str, data: ReactionUpdate):
    db_post = session.query(PostModel).filter(PostModel.id == post_id).first()
    db_user = session.query(UserModel).filter(UserModel.id == user_id).first()
    db_reaction = session.query(ReactionModel).filter(
        ReactionModel.userId == user_id).first()

    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    if db_reaction is None:
        raise HTTPException(status_code=404, detail='User not found')

    db_reaction.reaction = data.reaction
    session.commit()
    session.refresh(db_reaction)

    return db_reaction
