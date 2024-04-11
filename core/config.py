class Settings():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./db.sqlite3'
    USERS_OPEN_REGISTRATION = True

    FIRST_SUPERUSER_USERNAME: str = 'admin'
    FIRST_SUPERUSER_PASSWORD: str = 'admin'
    FIRST_SUPERUSER_EMAIL: str = 'admin@admin.com'


settings = Settings()
