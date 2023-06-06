#!/usr/bin/env python3
"""
define a _hash_password method
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    Returns a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Return a string representation of a new UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        should take mandatory email
        and password string arguments and return a User object
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(
                email=email, hashed_password=_hash_password(password)
            )
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate credentials
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        check = bcrypt.checkpw(password.encode(), user.hashed_password)
        return check
