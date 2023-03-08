import json
from flask import request, jsonify
from functools import wraps
import logging

class AuthorizationController:
    def __init__(self) -> None:
        pass

    def check_auth(self, username, password):
        if username == 'reports' and password == 'Welkom01!':
            return True
        print(f"NOT ALLOWED {username} with {password}")

    def human_login_required(self, f):
        @wraps(f)
        def wrapped_view(**kwargs):
            auth = request.authorization
            if not (auth and self.check_auth(auth.username, auth.password)):
                return ('Unauthorized', 401, {
                    'WWW-Authenticate': 'Basic realm="Login Required"'
                })
            return f(**kwargs)
        return wrapped_view

    def api_login_required(self, f):
        """ basic auth for api """
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth = request.authorization
            if not auth or not self.check_auth(auth.username, auth.password):
                if not auth:
                    print("Client didnot send auth header")
                return jsonify({'message': 'Authentication required'}), 401
            return f(*args, **kwargs)
        return decorated_function

