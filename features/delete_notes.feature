Feature: Delete notes
    As a user
    I want to delete a note
    So that I can remove my embarassing, juvenile philosophising from the record

    Scenario: Delete a note
        Given that there are notes:
        | first note    |
        | second note   |
        | third note    |
        When I delete the note with ID 1
        Then the response should be "Deleted note 1."
