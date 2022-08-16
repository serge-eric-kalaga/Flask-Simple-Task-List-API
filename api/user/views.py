from flask_restx import Resource, Namespace

user_namespace = Namespace("user", description="Namespace de User")

@user_namespace.route("/")
class UserGetCreate(Resource) : 
    
    def get(self):
        """Gets all users"""
        return {'message': 'User namespace'}
    
    def post(self):
        """Create a new user"""
        pass
                
    
    
@user_namespace.route("/<int:user_id>/")
class UserDeleteUpdateShow(Resource) : 
    
    def get(self, user_id):
        """Gets a user by id"""
        pass
    
    def delete(self, user_id):
        """Delete a user"""
        pass
    
    def put(self):
        """Update a user"""
        pass
        