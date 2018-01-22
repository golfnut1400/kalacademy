
'''
Homework 7
Create a NoteBook

# constructure of the class
every class
'''


'''
This represents a note in a Notebook

constructure of the class
self is a keyword. Helps to create an instance. only available to the function
it will save memory
object = instance of a class. Unable to create
memo,tag, and creationDate are 'properties'
testing using a separate file
  create a new file
  
  '''
#Initialize a note with memo and optional

#3tags separated by spaces



import datetime
last_id = 0

class Note:
    def __init__(self, memo, tags=""):

        self.memo = memo # using parameters
        self.tag = tags
        self.creationDate = datetime.date.today()
        # don't use print...just for development. Never add 'print' in a constructor
        global last_id  # use of global...must use or will cause an error
        last_id += 1    # add 1 for first run through
        self.id = last_id + 1
        print("Note Constructed", self.id, self.memo,self.creationDate)


