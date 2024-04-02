import requests


class TestUserRoutes:
    base_url = 'http://127.0.0.1:8000/users/'

    def test_get_all(self):
        response = requests.get(self.base_url)
        assert response.status_code == 200
        assert isinstance(response.json(), list)


class TestPostRoutes:
    base_url = 'http://127.0.0.1:8000/users/testcase/posts/'

    def test_get_all(self):
        response = requests.get(self.base_url)

        assert response.status_code == 200
        assert isinstance(response.json(), list)
