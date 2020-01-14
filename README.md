Behavior-Driven Development
==
Behavior-drive development, as the name implies, is a testing methodology that aims to
test software functionality over software internals.

An Example
===
Let's start off with an example.
Suppose we want to implement a note-taking service.
We'll keep its functionality pretty simple - our service should be able to:
1. Accept a string as a new note.
1. Return all notes along with a unique ID for each note.
1. Delete a note given its unique ID.

Now suppose we implemented this service as shown in the `src/note` package.
This command-line interface provides three functions:
```zsh
# Save a note with the next "This is the text of my note."
$ note save This is the text of my note.
# List all notes.
$ note list
# Delete the note with the unique identifier 14.
$ note delete 14
```

Supposing we know nothing else about this service, we would naturally want to test its
functionality to make sure we implemented our service as intended.
In this case we might write the following tests:
```python
def test_save_correctly_stores_note():
    <...>

def test_save_accepts_unicode():
    <...>

def test_list_correctly_returns_all_notes_and_ids():
    <...>

def test_delete_correctly_deletes_note():
    <...>

def test_delete_gives_correct_error_for_invalid_id():
    <...>

def test_delete_preserves_ids():
    <...>
```

This would seem natural.

But suppose now that we know the internals of the service (because we've looked at
`src/note` or - much worse - written some of `src/note`).
Then we might be tempted to write the following tests:
```python
# Data layer tests
def test_add_happy_path():
    <...>

def test_list_notes():
    <...>

def test_delete_happy_path():
    <...>

def test_delete_invalid_id():
    <...>


# CLI tests
mock_data_layer = mock(DataLayer)

def test_save_happy_path(DataLayer):
    <...>

def test_list(DataLayer):
    <...>

def test_delete_happy_path(DataLayer):
    <...>

def test_delete_invalid_id():
    <...>
```

These are tests for the internals of the application, and though they seem natural for
developers, they do have significant downsides.
A few bad tests can be seen in the `tests/` directory.
Tests such as these also need to be updated when the internals of the application are
changed.
When an intermediate interface is changed in the source code, two sets of tests - the
tests for the behavior of an implementation of the interface as well as all uses of that
interface.
An example of this issue can be seen with the `FileStore` interface.

Not only do unit tests provide less direct value than behavior tests, they also
encourage a pattern of mocking that often leads to undesired behavior slipping through
the test suite.
Some examples of this can be found in the `tests/` directory.
In particular, the `list_notes` method of the mock does not conform to the production
interface's method.
