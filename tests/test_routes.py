import unittest
import requests


class TestUserRoutes(unittest.TestCase):
    test_username = 'username'

    base_url = 'http://127.0.0.1:8000/users/'
    url_one = 'http://127.0.0.1:8000/users/username'
    url_signup = 'http://127.0.0.1:8000/users/signup'

    username_test = 'testUsername'
    password_test = 'testUsername'
    email_test = 'test@username.com'

    def test_get_all(self):
        response = requests.get(self.base_url)
        assert isinstance(response.json(), dict)
        assert response.status_code == 401

    def test_get_one(self):
        response = requests.get(self.url_one)
        assert isinstance(response.json(), dict)
        assert response.status_code == 401

    def test_put_one(self):
        response = requests.get(self.url_one)
        assert isinstance(response.json(), dict)
        assert response.status_code == 401

    def test_post_one(self):
        data = {
            "email": self.email_test,
            "username": self.username_test,
            "password": self.password_test
        }

        response = requests.post(self.url_signup, json=data)
        assert isinstance(response.json(), dict)
        assert response.status_code == 200

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
