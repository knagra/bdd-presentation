Feature: Delete notes
    As a user
    I want to delete a note
    So that I can remove my embarassing, juvenile philosophising from the record

    Scenario: Delete a note
        Given that there are notes:
        | note          |
        | first note    |
        | second note   |
        | third note    |
        When I delete the note with ID 1
        Then the response should be "Deleted note 1."

    Scenario: Delete a note that doesn't exist
        Given that there are notes:
        | note      |
        | note 1    |
        | note 2    |
        When I delete the note with ID 234
        Then the response should end with "Note with ID 234 does not exist."
