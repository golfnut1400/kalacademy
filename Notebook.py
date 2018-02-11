from Note import Note

class Notebook:
    '''
    Represent a collection of notes
    that can be tagged, modified, and searched
    '''

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        note = self.__find_note(note_id)
        note.memo = memo

    def modify_tags(self, note_id, tags):
        self.__find_note(note_id).tags = tags

    def __find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note

    def search(self, filter):
        '''
        Find all notes that match the given filter
        :param filter: filter clause
        :return: notes that match the filter
        '''
        return [note for note in self.notes if note.match(filter)]