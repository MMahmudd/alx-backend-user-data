#!/usr/bin/env python3
""" Module_of_Index_views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def authorized() -> str:
    """ GET_ /api/v1/unauthorized
    Return:
        - raise_a_401_error
    """
    abort(401, description="Unauthorized")


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbid() -> str:
    """ GET_/api/v1/forbidden
    Return:
        - raise_a_403_error
    """
    abort(403, description="Forbidden")


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET_ /api/v1/status
    Return:
      - the_status_of_the_API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET_ /api/v1/stats
    Return:
      - the_number_of_each_objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
