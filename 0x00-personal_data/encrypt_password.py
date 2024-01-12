#!/usr/bin/env python3
""" Encrypting_pswds_with_bcrypt """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Takes_in_string_arg,_converts_to_unicode
    Returns_salted,_hashed_pswd_as_bytestring
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks_if_hashed_and_unhashed_pswds_are_same
    Returns_bool
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
