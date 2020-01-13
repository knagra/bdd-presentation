import os
from datetime import datetime

class FileStore(object):

    DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

    def __init__(self, file_name=None):
        if file_name is None:
            file_name = "file_store.txt"
        self.file_name = file_name
        self.last_index = 0
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r+') as f:
                all_lines = f.readlines()
                if len(all_lines) > 0:
                    try:
                        self.last_index = int(all_lines[-1].split(' ', 1)[0])
                    except:
                        pass
        else:
            with open(self.file_name, 'a+') as f:
                pass
        super().__init__()

    def add_note(self, note):
        dt = datetime.now().strftime(self.DATETIME_FORMAT)
        with open(self.file_name, 'a') as f:
            f.write("{idx} {dt} {note}\n".format(
                idx=self.last_index + 1,
                dt=dt,
                note=note
            ))
        self.last_index += 1
        return self.last_index

    def list_notes(self):
        with open(self.file_name, 'r') as f:
            return list(map(lambda s: s.strip().split(' ', 2), f.readlines()))

    def delete_note(self, idx):
        all_notes = self.list_notes()
        notes = list()
        note_found = False
        for note in all_notes:
            note_idx = note.split(' ', 1)[0]
            if note_idx == idx:
                note_found = True
            else:
                notes.append(note)
        if not note_found:
            raise Exception("Note with ID {idx} does not exist.".format(idx=idx))
        with open(self.file_name, 'w+') as f:
            f.writelines(notes)
