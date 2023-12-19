import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or (
    "postgresql+psycopg://postgres:password@pg:5432/postgres"

)

engine = create_engine(url=PG_CONN_URI, echo=False)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    posts = relationship("Post", back_populates="user", uselist=True)


class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False)
    user = relationship("User", back_populates="posts", uselist=False)
