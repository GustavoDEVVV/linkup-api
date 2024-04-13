from sqlalchemy.orm import Session
from api.models.likes import ReactionModel
from api.models.users import UserModel


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
