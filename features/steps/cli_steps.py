from behave import given, when, then

@given('that there are notes')
def given_that_there_are_notes(context):
    pass

@when('I add a note "{note}"')
def given_i_add_a_note(context, note):
    pass

@when('I list notes')
def when_i_list_notes(context):
    pass

@then('the response should be "{message}"')
def then_the_response_should_be_successful(context, message):
    pass

@then('the response should be empty')
def then_the_response_should_be_empty(context):
    pass

@then('the response should be')
def then_the_response_should_be(context):
    pass
