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


if __name__ == '__main__':
    unittest.main()
