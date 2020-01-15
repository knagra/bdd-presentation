import subprocess
from behave import given, when, then


def execute_script(command, *args):
    cmd_list = ["python3", "src/note.py", command] + list(args)
    return subprocess.Popen(
        cmd_list,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

@given('that there are notes')
def given_that_there_are_notes(context):
    for row in context.table:
        context.proc = execute_script("save", row['note'])
        context.proc.wait()

@when('I add a note "{note}"')
def given_i_add_a_note(context, note):
    context.proc = execute_script("save", note)

@when('I list notes')
def when_i_list_notes(context):
    context.proc = execute_script("list")

@when('I delete the note with ID {note_id}')
def when_i_delete_the_note_with_id(context, note_id):
    context.proc = execute_script("delete", note_id)

@then('the response should be "{message}"')
def then_the_response_should_be_successful(context, message):
    out = context.proc.stdout.read().strip()
    assert out == message, out

@then('the response should be empty')
def then_the_response_should_be_empty(context):
    out = context.proc.stdout.read().strip()
    assert len(out) == 0, out

@then('the response should be')
def then_the_response_should_be(context):
    expected = " | ".join(context.table.headings) + "\n"
    for row in context.table:
        expected += " | ".join(row.cells) + "\n"
    actual = context.proc.stdout.read().strip()
    assert expected == actual, (expected, actual)
