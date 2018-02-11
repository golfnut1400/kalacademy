import datetime

#store the next available id for a new note
last_id = 0

class Note:
    '''
    Represent a note in the notebook.
    Match against a string in searches and store
    tags for each note.
    '''

    def __init__(self, memo, tags=''):
        '''
        Initialize a note with memo and optional
        space separated tags. Automatically set the
        note's creation date and a unique id.
        :param memo: memo of the note
        :param tags: space separated tags
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def __str__(self):
        return self.memo

    def match(self, filter):
        '''
        Determine if this note matches the filter
        text.
        :param filter: Search text. case sensitive search
        :return: Return True if matches, False otherwise.
        '''

        return filter in self.memo or filter in self.tags