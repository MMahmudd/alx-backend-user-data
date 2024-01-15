#!/usr/bin/env python3
""" Module_of_Index_views
"""
from flask import jsonify, abort
from api.v1.views import app_views


# unauthorized_access
@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """_su_mmary_

    Returns:
        str: _desc_ription_
    """
    abort(401, description='Unauthorized')

#_forbidden_
@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """_sum_mary_

    Ret_urns:
        str: _descr_iption_
    """
    abort(403, description='Forbidden')


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET_ /api/v1/status_
    Retu_rn:
      - the_status_of_the_API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET_/api/v1/stats_
    Return:
      - the_number_ of_each_objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
