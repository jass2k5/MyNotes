class Constants:
    def __init__(self,filename,taskname,notes):
        self.filename = filename
        self.taskname = taskname
        self.notes = notes
    
    def __str__(self):
        return f"name of task {self.taskname},note:{self.notes},file where the note is saved{self.filename}"
    

tester = Constants("notes.json","testing","testingnotes")
print(tester)