from asyncio import current_task

from src.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, \
    async_scoped_session


class DatabaseHelper:
    def __init__(self, url):
        self.engine = create_async_engine(url=url, echo=True)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autocommit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self):
        session = self.get_scoped_session()
        async with session() as s:
            yield s
        await session.close()


db_helper = DatabaseHelper(settings.DATABASE_URL)
