from flask_restx import Resource, Namespace
from ..user.views import user_namespace

task_namespace = Namespace('task', description="Namespace de Task")

@task_namespace.route("/")
class TaskGetCreate(Resource) : 
    
    def get(self):
        """""Get all the tasks"""
        pass
    
    def post(self):
        """Create a new task"""
        pass
        

@task_namespace.route("/<int:task_id>/")
class TaskShowUpdatedelete(Resource) :
    
    def get(self, task_id):
        """Get a task"""
        pass
    
    def delete(self, task_id):
        """Delete a task by id"""
        pass
    
    def update(self, task_id):
        """Update a task"""
        pass
    
    
@user_namespace.route("/<int:user_id>/tasks/")
class GetUserTasks(Resource) :
    
    def get(self, user_id):
        """Get all the tasks of specific user"""
        pass
        
        
@user_namespace.route("/<int:user_id>/tasks/<int:task_id>/")
class GetUserTask(Resource) :
    
    def get(self, user_id, task_id):
        """Get specific tasks of specific user"""
        pass
        
        
        
    
        