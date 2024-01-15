#!/usr/bin/env python3
"""
Module_for_authentication
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """_sum_mary_
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summ_ary_

        Args:
                pa_th (str): _descr_iption_
                excl_uded_p_aths (List_[str]): _des_cription_

        Retu_rns:
                b_ool: _de_scription_
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """_summ_ary_

        Args:
                re_quest (_type_,_optional): _desc_ription_. Def_aults to_None.

        Retur_ns:
                str: _desc_ription_
        """
        if request is None:
            return None
        # get header from the request
        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """_summ_ary_
        """

        return None
