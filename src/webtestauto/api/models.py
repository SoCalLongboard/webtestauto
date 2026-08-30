from typing import TypedDict


class User(TypedDict):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
