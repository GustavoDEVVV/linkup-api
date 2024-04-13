# fmt: off

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

from api.schemas.users import UserCreate
from api.models.users import UserModel
from api.crud.users import create_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest


class TestUserCrud(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        UserModel.metadata.create_all(engine)

        self.test_username = 'test'
        self.test_email = 'test@email.com'
        self.test_password = '123@123'

    def create_test_user(self):
        user = UserCreate(
            email=self.test_email,
            username=self.test_username,
            password=self.test_password
        )
        return create_user(session=self.session, user=user)

    def test_create_user(self):
        user_create = self.create_test_user()
        self.assertIsNotNone(user_create.id)


if __name__ == '__main__':
    unittest.main()
