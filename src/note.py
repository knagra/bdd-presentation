#!/usr/bin/python

from src.data.file_store import FileStore
import sys


class CLI(object):
    ERROR_MESSAGE = """
    Usage:
        note save <text of note>
        note list
        note delete <id of note>
    {message}"""

    def __init__(self, data_layer):
        self.data_layer = data_layer
        super().__init__()

    def error(self, message):
        print(self.ERROR_MESSAGE.format(message=message))

    def add_note(self, args):
        if len(args) < 3:
            error("note save requires text to save")
        note = ' '.join(args[2:])
        print("Added note {note_id}.".format(note_id=self.data_layer.add_note(note)))

    def list_notes(self, args):
        if len(args) > 2:
            error("note list received an unexpected argument")
        all_notes = self.data_layer.list_notes()
        print("added | index | note")
        for note in all_notes:
            print(" | ".join(note))

    def delete_note(self, args):
        if len(args) != 3:
            error("note delete expects only one argument, received {n}".format(
                n=len(args))
            )
        try:
            self.data_layer.delete_note(args[2])
        except Exception as exc:
            self.error(exc)
        else:
            print("Deleted note {note_id}.".format(note_id=args[2]))

COMMANDS = {
    "save": 'add_note',
    "list": 'list_notes',
    "delete": 'delete_note',
}

def main():
    if len(sys.argv) < 2:
        error("At least one of save, list, or delete must be cpass as a command")
        exit(1)
    if sys.argv[1] not in COMMANDS:
        error("Invalid command \"{command}\"".format(command=sys.argv[1]))
        exit(2)
    data_layer = FileStore("data_store.txt")
    cli = CLI(data_layer)
    getattr(cli, COMMANDS[sys.argv[1]])(sys.argv)


if __name__ == "__main__":
    main()
