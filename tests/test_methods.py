# fmt: off

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

from api.schemas.users import UserCreate, UserCreateSuperUser
from api.schemas.posts import PostCreate
from api.models.users import UserModel
from api.models.posts import PostModel
from api.crud.users import (create_super_user,
                            create_user,
                            delete_user,
                            get_user
                            )

from api.crud.posts import (insert_post, delete_post)

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
        user = UserCreate(
            email=self.test_email,
            username=self.test_username,
            password=self.test_password,
        )

        created_user = create_user(session=self.session, user=user)
        self.assertIsNotNone(created_user.id)


    def test_create_superuser(self):
        superuser = UserCreateSuperUser(
            email=self.test_email,
            username=self.test_username,
            password=self.test_password,
            is_superuser=True,
        )
        created_superuser = create_super_user(session=self.session, user=superuser)
        self.assertIsNotNone(created_superuser.id)


    def test_delete_user(self):
        user = UserCreate(
            email=self.test_email,
            username=self.test_username,
            password=self.test_password,
        )

        created_user = create_user(session=self.session, user=user)
        delete_user(session=self.session, user=created_user)
        deleted_user = get_user(session=self.session, user_id=created_user.id)

        self.assertIsNone(deleted_user)


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



if __name__ == '__main__':
    unittest.main()

