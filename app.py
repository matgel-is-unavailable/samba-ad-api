from flask import Flask
from controllers.authorizationcontroller import AuthorizationController
from controllers.appcontroller import AppController

version = "0.0.1"

class startup:
    def start(self):
        # Define flask app
        app = Flask(__name__)
        
        # Attach controllers
        auth = AuthorizationController()
        AppController(app, auth)

        # Run
        app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    program = startup()
    program.start()