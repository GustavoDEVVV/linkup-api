from sqlalchemy.orm import Session
from api.models import PostModel
from api.validators.post_validators import PostCreate


def select_posts(db: Session, username: str):
    return db.query(PostModel).filter(PostModel.owner_username == username).all()


def insert_post(db: Session, post: PostCreate, username: str):
    db_post = PostModel(**post.model_dump(), owner_username=username)

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return {"message": f"Post created at user = {db_post.id}"}
