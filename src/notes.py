
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
            self.note.append({
                "taskname": input_notename,
                "note": note_input,
                "save_time": timestamp
            })
            self.save_notes()#save instantly
            print(f"note added at {timestamp}")
    def show_stored(self):
        if self.note:
            for idx,line in enumerate(self.note,start = 1):
                print(f"{idx}:{line['taskname']} {line['note']} (saved on {line['save_time']})")
        else:
            print("no data found")
    def delete_note(self):
        print("e to exit")
        self.show_stored()
        while True:
            try:
                line = input("enter the no. of line you want to delete")
                n = get_checker(line)
                if n is None:
                    print("exiting")
                    return
                elif n <= 0 or n > len(self.note):
                    print("number is either 0 or greater than no. of notes in file")
                    continue
            except ValueError or TypeError:
                print("enter a valid digit")
            n = int(n)
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

            