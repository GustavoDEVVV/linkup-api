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

class TestPostRoutes:

    test_username = 'username'

    base_url = 'http://127.0.0.1:8000/users/'
    url_one = 'http://127.0.0.1:8000/users/username'
    url_signup = 'http://127.0.0.1:8000/users/signup'

    username_test = 'testUsername'
    password_test = 'testUsername'
    email_test = 'test@username.com'

    def get_auth_token(self):
        response = self.client.post('/login', data=json.dumps ({ #envia uma solicitação post para o login enviando email e senha do usuario
            'email': 'testuser@exemple.com',
            'password': 'password'
        }), content_type='application/json')

        data = json.loads(response.data) #converte os dados em json
        return data['access_token'] #retorna o token de accesso
    
    def test_creation_post(self):
        token = self.get_auth_token() #chama o token valido criado acima para solicitar a criação
        response = self.client.post('/post', data=json.dumps({
            'titulo': 'Testando Post',          #enviando uma solicitação para rota post e enviando o titulo e conteudo da mensagem em JSON, passa também o token  
            'conteudo': 'testando os posts'
        }), headers={'Autorização': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 201) #verifica se foi criado
        self.assertIn('id', json.loads(response.data)) #verifica se tem o campo id pra saber se foi criado o post

    def test_delet_post(self):

        token = self.get_auth_token() #pega o token de autenticação

        post_response = self.client.post('/post', data=json.dumps({ #faz uma solicitação a rota post enviando os dados e a autorização nas cabeças da aplicação
            'titulo': 'Testando Post',
            'conteudo': 'testando os posts'
        }), headers= {'Autorização': f'bearer {token}'}, content_type='application/json')
        post_id = json.loads(post_response.data)['id'] #extraindo o id post a partir da requisição

        delete_response = self.client.delete(f'/posts/{post_id}', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(delete_response.status_code, 204) #end point expecifico do post criado

        # Verify the post is deleted
        get_response = self.client.get(f'/posts/{post_id}', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(get_response.status_code, 404) #requisição get para o mesmo endpoint anterior


if __name__ == '__main__':
    unittest.main()
