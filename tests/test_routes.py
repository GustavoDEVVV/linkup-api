import requests


class TestUserRoutes:
    base_url = 'http://127.0.0.1:8000/users/'

    def test_get_all(self):
        response = requests.get(self.base_url)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        
    def test_get_user_by_username(self):
        username = 'Gustavo'
        response = request.get(f"{self.base_url}/{username}")
        assert request.status_code == 200
        assert isinstance(response.json, dict)

    def test_update_user(self):
        username = 'Gustavo'
        update_data_users = {'name': 'Gustavo', 'email': 'gustavo@example.com', 'password': '1234'}
        assert response.status_code == 200
        updated_user = response.json()
        assert updated_user['name'] == update_data_users['name']


class TestPostRoutes:

    base_url = 'http://127.0.0.1:8000/users/'

    def get_posts(username):

        url = f"{base_url}/users/{username}/posts/"
        response = requests.get(url)
        assert response.status_code == 200
        return response
   
    def test_update_post():
        id_post = 1
        update_data_post = {'username': 'Gustavo', 'id_post': 2}
        response = client.put(f"/posts/{id_post}", json=update_data_post)
        assert response.status_code == 200
        assert response.json()['id_post'] == update_data_post['id_post']