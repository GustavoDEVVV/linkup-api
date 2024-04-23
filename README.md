<p align="center">
  <!-- <img src="public/images/brand.png" height="128"> -->
  <h2 align="center">Linkup - API</h2>
  <p align="center">API for the social network Linkup API.<p>
</p>

![](https://i.imgur.com/waxVImv.png)

### Getting started

#### Required dependencies:

1. Python version 3.10 or higher
2. PIP version 22.2 or higher
3. GIT 2.41 or higher

#### First steps:

###### 1. Clone this repository

In your preferred directory, open a terminal and execute the following command:

`git clone https://github.com/JonathasSC/linkup-api`

Then, in the same terminal, run this command to navigate to the project directory:

`cd .\linkup-api\`

###### 2. Creating and activating a virtual enviroment:

1. `python -m venv venv`

2. `.\venv\Scripts\activate`

###### 2. Install project dependencies:

Still in the same terminal, run this command to install project libraries:

`pip install -r requirements.txt`

###### 3. Running API

After everything is installed correctly, run the command to start the API:

`uvicorn main:app --reload`

###### 4. API Docs:

To access the API documentation, navigate to:

`http://localhost:8000/docs`
Alternatively, for interactive documentation, navigate to:
`http://localhost:8000/redoc`

![](https://i.imgur.com/waxVImv.png)

#### Endpoints:

###### Auth

- POST - /login
- POST - /signup

###### Users

- GET - /users
- POST - /users
- GET - /users/{username}
- PUT - /users/{username}
- DELETE - /users/{username}

###### Posts

- GET - /users/{username}/posts
- POST - /users/{username}/posts
- DELETE - /users/{username}/posts/{post_id}

###### Reactions

- GET - /posts/{post_id}/reactions/
- POST - /posts/{post_id}/reactions/
- DELETE - /posts/{post_id}/reactions/

![](https://i.imgur.com/waxVImv.png)

#### Contributors

| Nome              | Commits |
| ----------------- | ------- |
| Jonathas Santos   | 76      |
| Gustavo Domingues | 8       |
| Caio Vinicius     | 8       |
| Esdras Brainer    | 2       |
| Pedro Freitas     | l       |
