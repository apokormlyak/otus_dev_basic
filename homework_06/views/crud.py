from ..models.models import User
from ..models.models import Post
from ..models.models import db


def create_user(
    name: str, username: str, email: str
) -> User:
    user = User(name=name, username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def get_users_list() -> list[User]:
    return User.query.all()


def get_user_by_id(user_id) -> User:
    return User.query.get_or_404(
        user_id,
        f'user {user_id} not found'
    )


def create_post(
    user_id: int, title: str, body: str
) -> Post:
    post = Post(user_id=user_id, title=title, body=body)
    db.session.add(post)
    db.session.commit()
    return post


def get_posts_list() -> list[Post]:
    return Post.query.all()


def get_post_by_id(post_id) -> Post:
    return Post.query.get_or_404(
        post_id,
        f'post {post_id} not found'
    )
