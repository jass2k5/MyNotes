
from src.utils.inputchecker import get_checker
import os
import json
from datetime import datetime

class Notes:
    def __init__(self,filename):
        self.filename = filename
        self.note = []
        #ensure the data folder exists 
           # Ensure data folder exists
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        # Load existing notes if file exists, else start empty
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            with open(self.filename, "w") as f:
                json.dump([], f)  # initialize empty list

        try:
            with open(self.filename, "r") as f:
                self.note = json.load(f)
        except json.JSONDecodeError:
            self.note = []  # fallback if file is empty or corrupted


    def save_notes(self):
        with open(self.filename,"w") as f:
            json.dump(self.note,f,indent =4)

    def add_note(self):
        #ensures the data folder exists
        while True:
            print(("enter e to exit"))
            notename = input("enter the name of your note").title().strip()
            input_notename = get_checker(notename)
            if input_notename is None:
                print("exiting...")
                return
            note_input = input("enter your note ").strip()
            timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
            edit = None
            self.note.append({
                "taskname": input_notename,
                "note": note_input,
                "save_time": timestamp,
                "edited_on": edit
            })
            self.save_notes()#save instantly
            print(f"note added at {timestamp}")
    def show_stored(self):
        if self.note:
            for idx,line in enumerate(self.note,start = 1):
                print(f"{idx}:{line['taskname']} {line['note']} (saved on {line['save_time']}) and (edited on {line['edited_on']})")
        else:
            print("no data found")
    def delete_note(self):
        self.show_stored()
        while True:
            exit_input = input("enter e to exist")
            exit = get_checker(exit_input)
            if exit is None:
                print("exiting...")
                return
            try:
                line = int(input("enter the no. of line you want to delete"))
                if line <= 0 or line > len(self.note):
                    print("number is either 0 or greater than no. of notes in file")
                    continue
            except (ValueError or TypeError):
                print("enter a valid digit")
            deleted = self.note.pop(line-1)
            self.save_notes()# didnt used del so we can print 
            print(f"deleted note:{deleted}")
    def delete_all_data(self):
        try:
            regulator = input("Type yes/No if you want to delete whole data\n⚠️your choices may have consequences").lower()
        except TypeError:
            print("write carefully ")
        if regulator == "yes":
            self.note.clear()
            self.save_notes()
            print("all data deleted succesfully")
        else:
            print("something went wrong try again later")
    def edit_the_note(self):
        if not self.note:
            print("no notes yet!")
            return
        print("showing all your notes......")
        print(f"there are total of {len(self.note)} notes")
        for idx, note in enumerate(self.note,start = 1):
            print(f"{idx}:{note['taskname']},{note['note']}, saved at {note['save_time']} edited on {note['edited_on']}")
        while True:
            print("enter e if you want to exit")
            numberfirst = input("enter the number of note u want to edit")
            number = get_checker(numberfirst)
            if number is None:
                print("exiting....")
                return
            try:
                number = int(number)
                if number <= 0 or number > len(self.note):
                    print("enter a valid number")
                    continue
            except (ValueError,TypeError):
                print("enter a valid number ")
                continue

            newtask = input("edit the taskname\nelse press enter to skip")      
            newnote = input("edit the note\nelse press enter to skip")
            if newnote:
                self.note[number-1]['note'] = newnote
            if newtask:
                self.note[number-1]['taskname'] = newtask
            if newnote or newtask:
                self.note[number-1]['edited_on'] =  datetime.now().strftime("%y-%m-%d %H:%M:%S")
                self.save_notes()
            break
                
            