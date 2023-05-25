#!/usr/bin/env python3
"""
Implement password encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that the provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
