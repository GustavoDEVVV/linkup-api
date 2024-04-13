from sqlalchemy.orm import Session
from api.models.likes import LikeModel
from api.models.users import UserModel


def create_like(session: Session, post_id: str, user_id: str, reaction: str):
    db_like = LikeModel(
        postId=post_id,
        userId=user_id,
        reaction=reaction
    )

    session.add(db_like)
    session.commit()
    session.refresh(db_like)

    return db_like


def get_likes_by_post_id(session: Session, post_id: str):
    return session.query(LikeModel).filter(LikeModel.postId == post_id).all()


def delete_like(session: Session, post_id: str, user_id: str):
    like = (
        session.query(LikeModel)
        .filter(LikeModel.postId == post_id, LikeModel.userId == user_id)
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
        .join(LikeModel, UserModel.id == LikeModel.userId)
        .filter(LikeModel.postId == post_id)
        .all()
    )
