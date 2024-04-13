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

    def test_get_user_by_username(self):
        username = 'Gustavo'
        response = requests.get(f"{create_engine}/{username}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_update_user(self):
        username = 'Gustavo'
        update_data_users = {'name': 'Gustavo', 'email': 'gustavo@example.com', 'password': '1234'}
        self.assertEqual(response.status_code, 200)
        self.assertEqual, update_user ['name'] == update_data_users['name']



class TestPostCrud(unittest.TestCase):


    def get_post(username):
        
        response = requests.get(create_engine)
        self.assertEqual(response.status_code, 200)
        return response

    def test_update_post(self):
        id_post = 1
        update_data_post = {'username': 'Gustavo', 'id_post': 2}
        response = requests.put(f"{self.base_url}/post{id_post}", json=update_data_post)
        self.assertEqual(response.status_code, 200)


    if __name__ == '__main__':
        unittest.main()
