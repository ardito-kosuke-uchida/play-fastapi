from . import accounts, posts

__all__ = ["routers"]
routers = [
    accounts.router,
    posts.router,
]

