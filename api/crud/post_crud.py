from sqlalchemy.orm import Session
from api.models import PostModel


def select_posts(db: Session, user_id: int):
    return db.query(PostModel).filter(PostModel.owner_id == user_id).all()
