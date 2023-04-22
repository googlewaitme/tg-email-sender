import gino

from tgbot.config import DbConfig
from tgbot.models import db

from tgbot.models import user
from tgbot.models import channel
from tgbot.models import email


async def create_db(config: DbConfig):
    await db.set_bind(f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:5432/{config.database}")
    await db.gino.create_all()
