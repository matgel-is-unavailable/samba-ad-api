from flask import Flask, render_template, request, Response, send_file, jsonify
from controllers.authorizationcontroller import AuthorizationController
from helpers.httpresponse import HttpResponse
from managers.sambaactivedirectorymanager import SambaActiveDirectoryManager

class AppController:
    
    def __init__(self, app : Flask, auth: AuthorizationController) -> None:
        self.app = app
        self.auth = auth
        self.init_controller()
        pass

    def init_controller(self):
        sambaActiveDirectoryManager = SambaActiveDirectoryManager()        
        @self.app.route('/api/createUser', methods=['POST'])
        @self.auth.api_login_required

        def createUser():
            try:
                args = request.args.to_dict()
                username = args.get("username")
                password = args.get("password")
                
                sambaActiveDirectoryManager = SambaActiveDirectoryManager()
                rdata = sambaActiveDirectoryManager.createUser(username, password)

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
        def updatePassword():
            try:
                args = request.args.to_dict()
                username = args.get("username")
                password = args.get("password")
                
                rdata = sambaActiveDirectoryManager.updatePassword(username, password)

                resp = jsonify(rdata)   # jsonify provides us with a full response
                resp.headers.add('Access-Control-Allow-Origin', '*')

                return resp

            except Exception as e: 
                raise e
                # 500 error
                return HttpResponse.getDefault(False)
        pass

