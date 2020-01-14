Feature: Add a note
    As a user
    I want to add a note
    So that I can retrieve and reflect on it later

    Scenario: Add a note and make sure it's stored
        Given that there are notes:
        | first note    |
        | second note   |
        | third note    |
        When I add a note "my added note"
        Then the response should be successful
        When I list notes
        Then the response should be:
        | first note    |
        | second note   |
        | third note    |
        | my added note |
