from core.config import settings
from core.database import get_db
from api.models.users import UserModel
from api.crud.users import create_super_user
from api.schemas.users import UserCreateSuperUser


async def init_db():

    session = next(get_db())

    existing_superuser = session.query(UserModel).filter(
        UserModel.username == settings.FIRST_SUPERUSER_USERNAME).first()

    if not existing_superuser:
        user_in = UserCreateSuperUser(
            is_superuser=True,
            username=settings.FIRST_SUPERUSER_USERNAME,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email=settings.FIRST_SUPERUSER_EMAIL,
        )

        create_super_user(session=session, user=user_in)
