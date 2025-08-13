from src.notes import Notes
def main():
    print("welcome to notebook")
    print("please enter your taskname")
    filename = "data/notes.json"
    access = Notes(filename)
    while True:
        try:
            ask = int(input("1: add, 2: show data, 3: delete a note, 4: delete all data"))
        except (ValueError or TypeError):
            print("enter valid number")
            continue
        if ask == 1:
            access.add_note()
        elif ask == 2:
            access.show_stored()
        elif ask == 3:
            access.delete_note()
        elif ask == 4:
            access.delete_all_data()
    
if __name__ == "__main__":
    main()