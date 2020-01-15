import unittest
from unittest.mock import mock_open, patch
from src.data.file_store import FileStore


class TestFileStore(unittest.TestCase):

    # Using a filename here that is different from the one we actually use in the source
    # can cause some errors that will not be caught by our tests.
    # For example, if we don't have read write access to the file.
    # Note that we aren't actually trying to access the file in the tests here, which
    # is much worse.
    # Even if we were trying to access the file system, we might still have errors as
    # mentioned above.
    TEST_FILE_NAME = "test_file_store.txt"

    def setUp(self):
        with patch('src.data.file_store.open', mock_open()):
            self.file_store = FileStore(self.TEST_FILE_NAME)

    def test_add_note(self):
        note_string = "This my note, and it is mine."
        mo = mock_open()
        with patch('src.data.file_store.open', mo):
            result = self.file_store.add_note(note_string)
        mo.assert_called_once_with(self.TEST_FILE_NAME, 'a')
        w = mo().write
        w.assert_called_once()
        idx, dt, n = w.call_args[0][0].split(' ', 2)
        assert idx == '1'
        assert n == note_string + '\n'
        assert result == 1

    def test_list_notes(self):
        # This is a bad test.
        # Our real add_note, as tested above, adds notes in the '{idx} {dt} {note}'
        # format, while this test expects data to be present in the '{dt} {idx} {note}'
        # format.
        # This test will pass and not alert us to the fact that our application will
        # print:
        # added | index | note
        # <idx> | <dt>  | <note>
        all_notes = "2008 1 My first note.\n" + \
            "2009 2 My second note.\n" + \
            "2013 5 My third note.\n"
        mo = mock_open(read_data=all_notes)
        with patch('src.data.file_store.open', mo):
            result = self.file_store.list_notes()
        mo.assert_called_once_with(self.TEST_FILE_NAME, 'r')
        r = mo().readlines
        r.assert_called_once()
        assert type(result) == list
        assert len(result) == 3
        assert result == [
            ["2008", "1", "My first note."],
            ["2009", "2", "My second note."],
            ["2013", "5", "My third note."],
        ], result

    def test_list_notes_backwards(self):
        # The functionality this method tests isn't actually used by any consumer of the
        # FileStore interface.
        # This test will give us the illusion that the functionality is actually used
        # and will promote cruft remaining in our interface.
        all_notes = "2008 1 My first note.\n" + \
            "2009 2 My second note.\n" + \
            "2013 5 My third note.\n"
        mo = mock_open(read_data=all_notes)
        with patch('src.data.file_store.open', mo):
            result = self.file_store.list_notes_backwards()
        mo.assert_called_once_with(self.TEST_FILE_NAME, 'r')
        r = mo().readlines
        r.assert_called_once()
        assert type(result) == list, type(result)
        assert len(result) == 3
        assert result == [
            ["2013", "5", "My third note."],
            ["2009", "2", "My second note."],
            ["2008", "1", "My first note."],
        ], result

    def test_delete_note(self):
        all_notes = "1 2001 note1\n" + \
            "2 2002 note2\n" + \
            "3 2003 note3\n"
        mo = mock_open(read_data=all_notes)
        with patch('src.data.file_store.open', mo):
            result = self.file_store.delete_note("2")
        assert mo.call_count == 2
        r = mo().readlines
        w = mo().writelines
        r.assert_called_once()
        w.assert_called_once_with(["1 2001 note1\n", "3 2003 note3\n"])

    def test_delete_invalid_id(self):
        all_notes = "1 2001 note1\n" + \
            "2 2002 note2\n" + \
            "4 2004 note4\n"
        mo = mock_open(read_data=all_notes)
        with patch('src.data.file_store.open', mo):
            self.assertRaises(Exception, self.file_store.delete_note, "3")
        assert mo.call_count == 1
        r = mo().readlines
        w = mo().writelines
        r.assert_called_once()
        w.assert_not_called()


if __name__ == '__main__':
    unittest.main()
