# fmt: off

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

from api.schemas.users import UserCreate, UserCreateSuperUser
from api.schemas.posts import PostCreate
from api.models.users import UserModel
from api.crud.users import (create_super_user,
                            create_user,
                            delete_user,
                            get_user,
                            get_user_by_email,
                            get_user_by_username,
                            select_users,
                            )

from api.crud.posts import insert_post
from api.crud.reactions import create_like, delete_like, get_likes_by_post_id, get_users_who_liked_post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest


class TestUserCrud(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///./test.sqlite3')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.test_username = 'test'
        self.test_password = '123@123'
        self.test_email = 'test@email.com'

        UserModel.metadata.drop_all(engine)
        UserModel.metadata.create_all(engine)

    def tearDown(self):
        self.session.close()

    def test_create_user(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        created_user = create_user(session=self.session, user=user)
        self.assertIsNotNone(created_user.id)


    def test_create_superuser(self):
        superuser = UserCreateSuperUser(email=self.test_email,
                                        username=self.test_username,
                                        password=self.test_password,
                                        is_superuser=True)

        created_superuser = create_super_user(session=self.session, user=superuser)
        self.assertIsNotNone(created_superuser.id)


    def test_delete_user(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        created_user = create_user(session=self.session, user=user)
        delete_user(session=self.session, user=created_user)
        deleted_user = get_user(session=self.session, user_id=created_user.id)

        self.assertIsNone(deleted_user)


    def test_get_user_by_email(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        created_user = create_user(session=self.session, user=user)
        user_by_email = get_user_by_email(session=self.session, email=created_user.email)

        self.assertIsNotNone(user_by_email.id)


    def test_get_user_by_username(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        created_user = create_user(session=self.session, user=user)
        user_by_username = get_user_by_username(session=self.session, username=created_user.username)

        self.assertIsNotNone(user_by_username.id)


    def test_select_users(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        create_user(session=self.session, user=user)

        selected_users = select_users(session=self.session, skip=0, limit=100)

        self.assertIsNotNone(selected_users)
        self.assertIsInstance(selected_users, list)


class TestPostCrud(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///./test.sqlite3')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.test_username = 'test'
        self.test_password = '123@123'
        self.test_email = 'test@email.com'

        self.test_title = 'Testando titulo!'
        self.test_description = 'Testando descrição!'

        UserModel.metadata.drop_all(engine)
        UserModel.metadata.create_all(engine)
        


    def tearDown(self):
        self.session.close()


    def test_create_post(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        post = PostCreate(description=self.test_description,
                          title=self.test_title)

        created_user = create_user(session=self.session, 
                                   user=user)

        created_post = insert_post(session=self.session, 
                                   username=created_user.username, 
                                   post=post)

        self.assertIsNotNone(created_post.id)
        
    def test_create_post(self):
    user = UserCreate(
        email=self.test_email,
        username=self.test_username,
        password=self.test_password,

    )

    post = PostCreate(
        description=self.test_description,
        title=self.test_title,
    )

    created_user = create_user(session=self.session,
                               user=user)

    created_post = insert_post(session=self.session,
                               username=created_user.username,
                               post=post)

    self.assertIsNotNone(created_post.id)

    def test_get_post_by_id(self):
    user = UserCreate(
        email=self.test_email,
        username=self.test_username,
        password=self.test_password,

    )

    post = PostCreate(
        description=self.test_description,
        title=self.test_title,
    )

    created_user = create_user(session=self.session,
       user=user)

    created_post = insert_post(session=self.session,
     username=created_user.username,
     post=post)

    post_by_id = get_post_by_id(session=self.session, post_id=created_post.id)

    self.assertIsNotNone(post_by_id)

    def test_delete_user(self):
    user = UserCreate(
      email=self.test_email,
      username=self.test_username,
      password=self.test_password,

    )

    post = PostCreate(
      description=self.test_description,
      title=self.test_title,
    )

    created_user = create_user(session=self.session,
     user=user)

    created_post = insert_post(session=self.session,
    username=created_user.username,
    post=post)

    delete_post(session=self.session, post=created_post)

    deleted_post = get_post_by_id(session=self.session, post_id=created_post.id)
    self.assertIsNone(deleted_post)


    def test_select_post(self):
    user = UserCreate(
      email=self.test_email,
      username=self.test_username,
      password=self.test_password,

    )

    post = PostCreate(
      description=self.test_description,
      title=self.test_title,
    )

    created_user = create_user(session=self.session,
     user=user)

    insert_post(session=self.session,
    username=created_user.username,
    post=post)

    selected_posts = select_posts(session=self.session, username=created_user.username)

    self.assertIsNotNone(selected_posts)

class TestReactionCrud(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///./test.sqlite3')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.test_username = 'test'
        self.test_password = '123@123'
        self.test_email = 'test@email.com'

        self.test_title = 'Testando titulo!'
        self.test_description = 'Testando descrição!'

        self.test_type = 'grr'

        UserModel.metadata.drop_all(engine)
        UserModel.metadata.create_all(engine)


    def tearDown(self):
        self.session.close()

    def test_create_reaction(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        post = PostCreate(description=self.test_description,
                          title=self.test_title)


        created_user = create_user(session=self.session,
                                   user=user)

        created_post = insert_post(session=self.session,
                                   username=created_user.username,
                                   post=post)

        created_reaction = create_like(self.session,
                                       user_id=created_user.id,
                                       post_id=created_post.id,
                                       reaction=self.test_type)

        self.assertIsNotNone(created_reaction.userId)

    def test_delete_reaction(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        post = PostCreate(description=self.test_description,
                          title=self.test_title)


        created_user = create_user(session=self.session,
                                   user=user)

        created_post = insert_post(session=self.session,
                                   username=created_user.username,
                                   post=post)

        create_like(self.session,
                    user_id=created_user.id,
                    post_id=created_post.id,
                    reaction=self.test_type)

        deleted_reaction = delete_like(self.session,
                                       user_id=created_user.id,
                                       post_id=created_post.id)

        self.assertEqual(deleted_reaction, {"message": "Like deleted successfully"})

    def test_get_likes_by_post_id(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        post = PostCreate(description=self.test_description,
                          title=self.test_title)


        created_user = create_user(session=self.session,
                                   user=user)

        created_post = insert_post(session=self.session,
                                   username=created_user.username,
                                   post=post)

        create_like(self.session,
                    user_id=created_user.id,
                    post_id=created_post.id,
                    reaction=self.test_type)

        get_reactions = get_likes_by_post_id(self.session,
                                             post_id=created_post.id)

        self.assertIsNotNone(get_reactions)

    def test_get_users_who_liked_post(self):
        user = UserCreate(email=self.test_email,
                          username=self.test_username,
                          password=self.test_password)

        post = PostCreate(description=self.test_description,
                          title=self.test_title)


        created_user = create_user(session=self.session,
                                   user=user)

        created_post = insert_post(session=self.session,
                                   username=created_user.username,
                                   post=post)

        get_users_who_liked = get_users_who_liked_post(self.session,
                                                       post_id=created_post.id)

        self.assertIsNotNone(get_users_who_liked) 

if __name__ == '__main__':
    unittest.main()