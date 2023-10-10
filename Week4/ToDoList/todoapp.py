from todo import Todo

#assuming the todo file is in another folder named models then u do from models.todo import Todo

class TodoApp:
    #list of todo objects 
    todos = []

    def start():
        print("starting -- app......")
        print("*" * 20)

    def addTask(task: Todo):
        pass
    
    def editTask(task: Todo):
        pass

    def removeTask(task : Todo):
        pass
    def viewTask(task: Todo):
        pass 
    def viewAllTasks():
        return TodoApp.todos
    def stopTask():
        exit

TodoApp.start()

#clone repo
#create your own branch
#and create a merge request
    
