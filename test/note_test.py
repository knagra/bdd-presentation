from io import StringIO
import unittest
from unittest.mock import Mock, patch
from src.note import CLI


class TestCLI(unittest.TestCase):

    def setUp(self):
        self.data_layer = Mock()
        self.cli = CLI(self.data_layer)

    def test_add_note(self):
        self.data_layer.add_note.return_value = 1
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.add_note(["", "", "my", "note"])
            output = fake_out.getvalue()
            assert output == "Added note 1.\n", output
        self.data_layer.add_note.assert_called_once_with("my note")

    def test_list_notes(self):
        # This is a bad test. The real FileStore returns tuples of form
        # (<idx>, <datetime>, <note string>)
        # while our mock returns items of form
        # (<datetime>, <idx>, <note string>)
        # In this case, our tests won't alert us to the issue of misordered printing.
        self.data_layer.list_notes.return_value = [
            ("7", "1", "my note"),
            ("11", "2", "second note"),
        ]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.list_notes(["", ""])
            output = fake_out.getvalue()
            assert output == "length | index | note\n" + \
                "7 | 1 | my note\n" + \
                "11 | 2 | second note\n"
        self.data_layer.list_notes.assert_called_once_with()

    def test_delete_note(self):
        self.data_layer.delete_note.return_value = ""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.delete_note(["", "", "1"])
            output = fake_out.getvalue()
            assert output == "Deleted note 1.\n"
        self.data_layer.delete_note.assert_called_once_with("1")

if __name__ == "__main__":
    unittest.main()
