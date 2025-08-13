from src.notes import Notes
from src.constant import Constants

print("welcome to notebook")
print("please enter your taskname")
task = input("enter the name of your note")
filename = "data/notes.json"
access = Notes(filename,task)
while True:
    try:
        ask = int(input("1: add, 2: "))
    except (ValueError or TypeError):
        print("enter valid number")
        continue
    if ask == 1:
        access.add_note()

    