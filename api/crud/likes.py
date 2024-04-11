from sqlalchemy.orm import Session
from api.models import LikeModel, UserModel
from api.validators.like_validators import LikeCreate


def create_like(db: Session, post_id: str, user_id: str):
    like = LikeModel(postId=post_id, userId=user_id)
    db.add(like)
    db.commit()
    db.refresh(like)
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
