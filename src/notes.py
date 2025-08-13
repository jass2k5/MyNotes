from src.constant import Constants
from src.utils.inputchecker import get_checker
import os
import json
from datetime import datetime

class Notes:
    def __init__(self,filename,taskname):
        self.data = Constants(filename,taskname)
        self.note = []
        #ensure the data folder exists 
           # Ensure data folder exists
        os.makedirs(os.path.dirname(self.data.filename), exist_ok=True)

        # Load existing notes if file exists, else start empty
        if not os.path.exists(self.data.filename) or os.stat(self.data.filename).st_size == 0:
            with open(self.data.filename, "w") as f:
                json.dump([], f)  # initialize empty list

        try:
            with open(self.data.filename, "r") as f:
                self.note = json.load(f)
        except json.JSONDecodeError:
            self.note = []  # fallback if file is empty or corrupted


    def save_notes(self):
        with open(self.data.filename,"w") as f:
            json.dump(self.note,f,indent =4)

    def add_note(self):
        #ensures the data folder exists
        while True:
            note_input = input("enter your note ")
            input_note = get_checker(note_input)
            if input_note is None:
                print("exiting...")
                return
            timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
            self.note.append({
                "note": input_note,
                "save_time": timestamp
            })
            self.save_notes()#save instantly
            print(f"note added at {timestamp}")
    def show_stored(self):
        if self.note:
            for idx,line in enumerate(self.note,start = 1):
                print(f"{idx}: {line['note']} (saved on {line['save_time']})")
        else:
            print("no data found")
