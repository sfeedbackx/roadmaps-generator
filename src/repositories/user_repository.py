import asyncio
from prisma import Prisma
from ..models import UserCreate, User, UserBase


class UserRepository:
    def __init__(self, db: Prisma):
        self.db = db

    async def get_user_by_id(self, user_id: str) -> User:
        fond_user = await self.db.user.find_unique(where={"id": user_id})
        return User(**(fond_user.model_dump()))

    async def create_user(self, user: UserCreate):
        return await self.db.user.create(data=user.model_dump())


async def main():
    db = Prisma()
    await db.connect()

    try:
        repo = UserRepository(db)
        found_user = await repo.get_user_by_id("cmja6lxan000074fgbz3mr72a")
        print(found_user.model_dump())
    finally:
        await db.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
