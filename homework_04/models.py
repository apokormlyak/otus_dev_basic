"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

PG_CONN_URI = (os.environ.get("SQLALCHEMY_PG_CONN_URI")
               or ("postgresql+asyncpg://postgres:password@0.0.0.0:5432/postgres"))

async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=False
)

Session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id = Column(
        Integer,
        primary_key=True
    )


class User(Base):
    name = Column(
        String,
        nullable=False
    )
    username = Column(
        String,
        nullable=False,
        unique=True
    )
    email = Column(
        String,
        nullable=True,
        unique=True
    )
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True
    )


class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )
    title = Column(
        String,
        nullable=False,
        default="",
        server_default=""
    )
    body = Column(
        String,
        nullable=False
    )
    user = relationship(
        "User",
        back_populates="posts",
        uselist=False
    )

