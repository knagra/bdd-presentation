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
