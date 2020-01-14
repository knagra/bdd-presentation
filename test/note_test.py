from io import StringIO
from unittest import TestCase
from unittest.mock import Mock, patch
from src.note import CLI


class TestCLI(TestCase):

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
        self.data_layer.list_notes.return_value = [
            ("2008", "1", "my note"),
            ("2009", "2", "second note"),
        ]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.list_notes(["", ""])
            output = fake_out.getvalue()
            assert output == "added | index | note\n" + \
                "2008 | 1 | my note\n" + \
                "2009 | 2 | second note\n"
        self.data_layer.list_notes.assert_called_once_with()

    def test_delete_note(self):
        self.data_layer.delete_note.return_value = ""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.delete_note(["", "", "1"])
            output = fake_out.getvalue()
            assert output == "Deleted note 1.\n"
        self.data_layer.delete_note.assert_called_once_with("1")
