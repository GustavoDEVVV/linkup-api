from sqlalchemy.orm import Session
from api.models.posts import PostModel
from api.schemas.posts import PostCreate


def select_posts(session: Session, username: str):
    return session.query(PostModel).filter(PostModel.owner_username == username).all()


def insert_post(session: Session, username: str, post: PostCreate):
    db_post = PostModel(
        title=post.title,
        description=post.description,
        owner_username=username
    )

    session.add(db_post)
    session.commit()
    session.refresh(db_post)

    return {"message": f"Post created"}
