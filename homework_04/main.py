"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import jsonplaceholder_requests
from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from models import Post
from models import Session
from typing import List


async def create_user(
    session: AsyncSession, name: str, username: str, email: str
) -> User:
    user = User(name=name, username=username, email=email)
    session.add(user)
    await session.commit()
    return user


async def create_users(session: AsyncSession, users: list) -> list[User]:
    users_list = [
        User(name=user["name"], username=user["username"], email=user["email"])
        for user in users
    ]
    session.add_all(users_list)
    await session.commit()
    return users_list


async def create_post(
    session: AsyncSession, user_id: int, title: str, body: str
) -> Post:
    post = Post(user_id=user_id, title=title, body=body)
    session.add(post)
    await session.commit()
    return post


async def create_posts(session: AsyncSession, posts: list) -> list[Post]:
    posts_list = [
        Post(user_id=post["userId"], title=post["title"], body=post["body"])
        for post in posts
    ]
    session.add_all(posts_list)
    await session.commit()
    return posts_list


async def async_main():
    # Base.metadata.drop_all(bind=async_engine)
    # Base.metadata.create_all(bind=async_engine)
    async with Session() as session:
        posts_data: List[dict]
        users_data: List[dict]
        users_data, posts_data = await asyncio.gather(
            jsonplaceholder_requests.get_users(), jsonplaceholder_requests.get_posts()
        )
        await create_users(session, users_data)
        await create_posts(session, posts_data)


if __name__ == "__main__":
    asyncio.run(async_main())
