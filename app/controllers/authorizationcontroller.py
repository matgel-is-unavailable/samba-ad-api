import json
from flask import request, jsonify
from functools import wraps
import logging
import getpass
#import ldb
from samba.auth import system_session
from samba.credentials import Credentials
from samba.dcerpc import security
from samba.dcerpc.security import dom_sid
from samba.ndr import ndr_pack, ndr_unpack
from samba.param import LoadParm
from samba.samdb import SamDB
from typing import List
from unittest import result

class AuthorizationController:
    def __init__(self) -> None:
        pass

    def check_auth(self, username, password):
        # Allow only Administrator account
        if username.capitalize() == "Administrator":
            lp = LoadParm()
            creds = Credentials()
            creds.guess(lp)
            creds.set_username(username)
            creds.set_password(password)
            try:
                samdb = SamDB(url='ldap://10.1.0.2:389', session_info=system_session(),credentials=creds, lp=lp)
            except:
                print(f"NOT ALLOWED {username} with {password}")
            else:
                return True

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
            if not auth:
                return jsonify({'message': 'Authentication required'}), 401
            if not self.check_auth(auth.username, auth.password):
                return jsonify({'message': 'Wrong login/password. Only Administrator account is allowed!'}), 401
            return f(*args, **kwargs)
        return decorated_function

