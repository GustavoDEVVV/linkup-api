from sqlalchemy.orm import Session
from api.models.posts import PostModel
from api.schemas.posts import PostCreate, PostUpdate


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

    return db_post


def delete_post(session: Session, post: PostCreate):
    session.delete(post)
    session.commit()


def get_post_by_id(session: Session,  post_id: str):
    return session.query(PostModel).filter(PostModel.id == post_id).first()


def update_post(session: Session, post_id: str, data: PostUpdate):
    db_post = session.query(PostModel).filter(PostModel.id == post_id).first()
    db_post.title = data.title
    db_post.description = data.description
    session.commit()
    session.refresh(db_post)

    return db_post
