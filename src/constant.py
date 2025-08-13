class Constants:
    def __init__(self,filename,taskname):
        self.filename = filename
        self.taskname = taskname
    
    def __str__(self):
        return f"name of task {self.taskname},note:{self.note},file where the note is saved{self.filename}"
    

