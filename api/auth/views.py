from flask_restx import Resource, Namespace

auth_namespace = Namespace("auth", description="A namespace for authentication")

@auth_namespace.route('/register/')
class Register(Resource):
    
    def post(self):
        """Register a new user """
        pass
    

@auth_namespace.route('/login/')
class Register(Resource):
    
    def post(self):
        """Login and cre token"""
        pass
    
