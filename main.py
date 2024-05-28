def main_menu():
    print("\nNotebook")
    print("1. Add new note")
    print("2. Check all notes")
    print("3. Delete note")
    print("4. Close notebook")
    choice = input("Select action: ")
    return choice

def add_note(): #function to add note
    note = input("Insert note: ")
    notes.append(note)
    print("Note successfully added!")

def view_notes(): #function to check all notes
    if not notes:
        print("There are no notes")
    else:
        print("\nAll notes:")
        for idx, note in enumerate(notes, start=1): #print notes by order adding index number to it
            print(f"{idx}. {note}")

def delete_note(): #function to delete note
    if not notes:
        print("There is no notes to delete.")
    else:
        view_notes()
        try:
            index = int(input("Enter note number, that You would like to delete: ")) - 1
            if 0 <= index < len(notes):
                removed_note = notes.pop(index)
                print(f"Note '{removed_note}' successfully deleted.")
            else:
                print("Wrong number.")
        except ValueError:
            print("Enter number of note You would like to delete.")


notes = []  #variable to add values

while True: #main program to start cycle for users choice
    choice = main_menu()

    if choice == '1':
        add_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        delete_note()
    elif choice == '4':
        print("Exiting program")
        break
    else:
        print("Wrong choice, try one more time.")
