import aiohttp

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def get_users():
    data = await fetch_json(USERS_DATA_URL)
    users = []
    for user in data:
        user_data = {k: v for k, v in user.items() if k in ['name', 'username', 'email']}
        users.append(user_data)
    return users


async def get_posts():
    data = await fetch_json(POSTS_DATA_URL)
    posts = []
    for post in data:
        post_data = {k: v for k, v in post.items() if k in ['userId', 'title', 'body']}
        posts.append(post_data)
    return posts
