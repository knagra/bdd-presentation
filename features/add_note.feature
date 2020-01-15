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
        Then the response should be "Added note 4."
        When I list notes
        Then the response should be:
        | first note    |
        | second note   |
        | third note    |
        | my added note |

    Scenario: Add a note with no notes currently present
        When I add a note "my added note"
        Then the response should be "Added note 4."
        When I list notes
        Then the response should be:
        | idx   | length    | note      |
