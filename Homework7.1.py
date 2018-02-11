

from Homework7 import Note, Notebook
import sys

#
# class Menu:
#     def __init__(self):
#         self.notebook = Notebook()
#         self.choices = {
#             "1": self.show_notes,
#             "2": self.search_notes,
#             "3": self.add_note,
#             "4": self.modify_note,
#             "5": self.quit
#
#         }

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            #"1": self.quit


            "5": self.shownotes

        }

    def display_menu(self):

        # use of """ in the print statement to take literally
        print("""
        
        Note Menu
        
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")

            action = self.choices.get(choice)
        #delegate
            if action:
                action()
            else:
                    print("{} is not a valid choice".format(choice))



   def show_notes(self, notes=None):
       if not notes:
           notes = self.notebook.notes

       for note in notes:
           print("{0}: {1}\n{2}".format(note.id, note.memo, note.tags))

    def search_notes(self):
        filter = input("Search for: ")
        matchNotes = self.notebook.search(filter)
        self.show_notes(matchNotes)


    def add_notes(self):
        memo = input("Enter text in the memo")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id = int(input("Enter a note id: "))
        memo = input ("Enter a memo: ")
        tags = input ("Enter a tags: ")

        if memo:
            self.notebook.modify_memo(id, memo)

        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using the notebook")
        #exit using sys import
        sys.exit(0)

# store class in the menu variable
menu = Menu()
# executes the run() function within the menu
menu.run()
