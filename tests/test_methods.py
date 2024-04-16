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


class Utils:
    def __init__(self) -> None:
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        UserModel.metadata.create_all(engine)
        PostModel.metadata.create_all(engine)

        self.test_username = 'test'
        self.test_email = 'test@email.com'
        self.test_password = '123@123'

        self.test_title = 'Testando titulo!'
        self.test_description = 'Testando descrição!'

    def create_test_user(self):
        user = UserCreate(
            email=self.test_email,
            username=self.test_username,
            password=self.test_password,

        )
        return create_user(session=self.session, user=user) 

    def create_test_super_user(self):
        user = UserCreateSuperUser(
            email=self.test_email,
            username=self.test_username,
            password=self.test_password,
            is_superuser=True,
        )
        return create_super_user(session=self.session, user=user)

    def create_test_post(self):
        user_create = self.create_test_user()

        post = PostCreate(
            description=self.test_description,
            title=self.test_title,
        )
        return insert_post(
                        session=self.session,
                        username=user_create.username,
                        post=post, 
                        )


# ==========================================================

class TestUserCrud(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.utils = Utils()
        super().__init__(methodName)

    def test_create_user(self):
        user_create = self.utils.create_test_user()
        self.assertIsNotNone(user_create.id)

    def test_delete_user(self):
        user_create = self.utils.create_test_user()
        delete_user(session=self.utils.session, user=user_create)
        user_deleted = get_user(session=self.utils.session, user_id=user_create.id)
        self.assertIsNone(user_deleted)

    def test_create_super_user(self):
        superuser_create = self.utils.create_test_super_user()
        self.assertIsNotNone(superuser_create.id)

# ----------------------------------------------------------

class TestPostCrud(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.utils = Utils()
        super().__init__(methodName)

    def test_create_post(self):
        post_create = self.utils.create_test_post()
        self.assertIsNotNone(post_create.id)

# ==========================================================

    if __name__ == '__main__':
        unittest.main()
