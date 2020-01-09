class FileStore(object):
    def __init__(self, file_name=None):
        if file_name is None:
            file_name = "file_store.txt"
        self.file_name = file_name
        self.last_index = 0
        with open(self.file_name, 'w+') as f:
            all_lines = f.readlines()
            if len(all_lines) > 0:
                try:
                    self.last_index = int(all_lines[-1].split(' ', 1)[0])
                except:
                    pass
        super().__init__()

    def add(self, note):
        with open(self.file_name, 'a+') as f:
            f.write("{idx} {note}\n".format(idx=self.last_index + 1, note=note))
        self.last_index += 1
        return self.last_index

    def list(self):
        with open(self.file_name, 'r') as f:
            all_lines = f.readlines()
        notes = list()
        for line in all_lines:
            parsed = line.split(' ', 1)
            notes.append(Note(note_id=parsed[0], text=parsed[1]))
        return notes

    def delete(self, idx):
        with open(self.file_name, 'w') as f:
            all_lines = f.readlines()
            notes = list()
            for line in all_lines:
                line_idx = line.split(' ', 1)[0]
                if line_idx != idx:
                    notes.append(line)
            f.writelines(notes)
