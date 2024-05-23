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

    def test_post_one(self):
        data = {
            "email": self.email_test,
            "username": self.username_test,
            "password": self.password_test
        }

        response = requests.post(self.url_signup, json=data)
        assert isinstance(response.json(), dict)
        assert response.status_code == 200

class TestPostRoutes:

    test_username = 'username'

    base_url = 'http://127.0.0.1:8000/users/'
    url_one = 'http://127.0.0.1:8000/users/username'
    url_signup = 'http://127.0.0.1:8000/users/signup'

    titulo_teste: 'Testando_Post'
    password_test = 'testUsername'
    email_test = 'test@username.com'
    conteudo_teste: 'testando_os_posts'

    def get_auth_token(self):
        response = self.client.post('/login', data=json.dumps ({
            "email": self.email_test,
            "password": self.password_test
        }), content_type='application/json')

        data = json.loads(response.data)
        return data['access_token']
    
    def test_creation_post(self):
        token = self.get_auth_token()
        response = self.client.post('/post', data=json.dumps({
            'titulo': self.titulo_teste,
            'conteudo': self.conteudo_teste
        }), headers={'Autorização': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_delet_post(self):

        token = self.get_auth_token()

        post_response = self.client.post('/post', data=json.dumps({
            'titulo': self.titulo_teste,
            'conteudo': self.conteudo_teste
        }), headers= {'Autorização': f'bearer {token}'}, content_type='application/json')
        post_id = json.loads(post_response.data)['id']

        delete_response = self.client.delete(f'/posts/{post_id}', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(delete_response.status_code, 204)

        get_response = self.client.get(f'/posts/{post_id}', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(get_response.status_code, 404) 


if __name__ == '__main__':
    unittest.main()
