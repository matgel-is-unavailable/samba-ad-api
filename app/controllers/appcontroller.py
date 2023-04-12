from flask import Flask, render_template, request, Response, send_file, jsonify
from controllers.authorizationcontroller import AuthorizationController
from helpers.httpresponse import HttpResponse
from api.userManagement import *
from api.gpoManagement import *

class AppController:
    def __init__(self, app : Flask, auth: AuthorizationController) -> None:
        self.app = app
        self.auth = auth
        self.init_controller(self.auth)
        pass

    def init_controller(self, auth):
        @self.app.route('/api/createUser', methods=['POST'])
        @self.auth.api_login_required
        def callCreateUser():
            try:
                args = request.args.to_dict()
                username = args.get("username")
                password = args.get("password")
                samdb = auth.get_auth()
                rdata = createUser(username, password, samdb)
                resp = jsonify(rdata)   # jsonify provides us with a full response
                resp.headers.add('Access-Control-Allow-Origin', '*')
                return resp
            except Exception as e: 
                raise e
                # 500 error
                return HttpResponse.getDefault(False)
            pass

        @self.app.route('/api/updatePassword', methods=['POST'])                
        @self.auth.api_login_required
        def callUpdatePassword():
            try:
                args = request.args.to_dict()
                username = args.get("username")
                password = args.get("password")
                samdb = auth.get_auth()
                rdata = updatePassword(username, password, samdb)
                resp = jsonify(rdata)   # jsonify provides us with a full response
                resp.headers.add('Access-Control-Allow-Origin', '*')
                return resp

            except Exception as e: 
                raise e
                # 500 error
                return HttpResponse.getDefault(False)
        pass

        @self.app.route('/api/deleteUser', methods=['POST'])
        @self.auth.api_login_required
        def callDeleteUser():
            try:
                args = request.args.to_dict()
                username = args.get("username")
                samdb = auth.get_auth()
                rdata = deleteUser(username, samdb)
                resp = jsonify(rdata)   # jsonify provides us with a full response
                resp.headers.add('Access-Control-Allow-Origin', '*')
                return resp
            except Exception as e: 
                raise e
                # 500 error
                return HttpResponse.getDefault(False)
            pass

        @self.app.route('/api/listActiveUsers', methods=['GET'])
        @self.auth.api_login_required
        def callListActiveUsers():
            try:
                samdb = auth.get_auth()
                rdata = listUsers(samdb)
                resp = jsonify(rdata) # jsonify provides us with a full response
                resp.headers.add('Access-Control-Allow-Origin', '*')
                return resp
            except Exception as e: 
                raise e
                # 500 error
                return HttpResponse.getDefault(False)
            pass
    
        @self.app.route('/api/listGPO', methods=['GET'])
        @self.auth.api_login_required
        def callListGPO():
            try:
                samdb = auth.get_auth()
                rdata = listGPO(samdb)
                resp = jsonify(rdata) # jsonify provides us with a full response
                resp.headers.add('Access-Control-Allow-Origin', '*')
                return resp
            except Exception as e: 
                raise e
                # 500 error
                return HttpResponse.getDefault(False)
            pass
    
        

