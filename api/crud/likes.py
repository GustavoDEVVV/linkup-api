from sqlalchemy.orm import Session  # type: ignore
from api.models.likes import LikeModel
from api.models.users import UserModel
from api.schemas.likes import LikeCreate


def create_like(session: Session, post_id: str, user_id: str, reaction: str):
    like = LikeModel(postId=post_id, userId=user_id, reaction=reaction)
    session.add(like)
    session.commit()
    session.refresh(like)
    return like


def get_likes_by_post_id(db: Session, post_id: str):
    return db.query(LikeModel).filter(LikeModel.postId == post_id).all()


def delete_like(db: Session, post_id: str, user_id: str):
    like = (
        db.query(LikeModel)
        .filter(LikeModel.postId == post_id, LikeModel.userId == user_id)
        .first()
    )
    if like:
        db.delete(like)
        db.commit()
        return {"message": "Like deleted successfully"}
    else:
        return {"message": "Like not found"}


def get_users_who_liked_post(db: Session, post_id: str):
    return (
        db.query(UserModel)
        .join(LikeModel, UserModel.id == LikeModel.userId)
        .filter(LikeModel.postId == post_id)
        .all()
    )
