#!/usr/bin/env python3
"""
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
