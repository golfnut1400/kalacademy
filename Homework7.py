
'''
Homework 7
Create a NoteBook

USE THIS PROGRAM WITH HOMEWORK7.1.PY FILE

# constructure of the class
every class
'''


'''
This represents a note in a Notebook

constructure of the class
'self' is a keyword. Helps to create an instance. only available to the function
it will save memory
object = instance of a class.
memo,tag,and creationDate are 'properties'
testing using a separate file
  create a new file
  
  '''
#Initialize a note with memo and optional

#3tags separated by spaces



import datetime
last_id = 0

# Create a Note class
class Note:
    def __init__(self, memo, tags=""):
        # creation of the properties of the class
        self.memo = memo # using parameters
        self.tags = tags
        self.creationDate = datetime.date.today()
        # don't use print...just for development. Never add 'print' in a constructor
        global last_id  # use of global...must use or will cause an error
        last_id += 1    # add 1 for first run through
        self.id = last_id + 1
        self.tag = "I am a tag"
        # prints out all the values
        print("Note Constructed", self.id, self.memo,self.creationDate,self.tag)

   # __ underscore means this is private
    # this means to turn the object into a string
    # (self) points to the memory of the object
    def __str__(self):
        return self.memo


    # to be used for searching. There is no underscore (special). to be used outsite the class
    # this check if will match the filter
    # :param filter: search text. case sensitive search
    # :return TRUE if matches, FALSE otherwise
    def match(self, filter):
        return filter in self.memo or filter in self.tags


# this will hold the notes (array)
class Notebook:

    def __init__(self):
        self.notes = []   # collection - will hold notes.



        # add note to notebook
    def new_note(self, memo, tags=""):
        n = Note(memo,tags)
        # will store in the notebook
        self.notes.append(n)


    def modify_memo(self, note_id, memo):
       note = self.__find_notes(note_id)
       if not note:
           print("Note no found. try again")
       else:
           note.memo = memo


    def modify_tags(self, note_id, tags):
       tag = self.__find_notes(note_id)
       if not note:
           print("Note no found. try again")
       else:
           note.tags = tags

        #this is a private function. Can only be used with in this class due to the __ underscore
    def __find_notes(self, note_id):
        for note in self.notes:
            if note.id == note.id:
                return note
        return None



    def search(self,filter):
        # for n in range(self.notes):
        #     if n.match(filter) == True:
        #         return True
        #
        # return False
        # Find all notes that match the given filter
        # param filter: /filter clause
        # return: notes that match the filter
        #
        return [note for note in self.notes if note.match(filter)]


