#!/usr/bin/env python3
"""
Module of session auth views
"""
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    create login route
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) < 1:
        return jsonify({"error": "no user found for this email"}), 404
    if users[0].is_valid_password(pwd):
        from api.v1.app import auth
        sessionId = auth.create_session(getattr(users[0], 'id'))
        resp = jsonify(users[0].to_json())
        resp.set_cookie(getenv('SESSION_NAME'), sessionId)
        return resp
    return jsonify({"error": "wrong password"}), 401
