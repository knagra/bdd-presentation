Feature: Add a note
    As a user
    I want to add a note
    So that I can retrieve and reflect on it later

    Scenario: Add a note and make sure it's stored
        Given that there are notes:
        | note          |
        | first note    |
        | second note   |
        | third note    |
        When I add a note "my added note"
        Then the response should be "Added note 4."
        When I list notes
        Then the response should be:
        | index | length    | note          |
        | 1     | 10        | first note    |
        | 2     | 11        | second note   |
        | 3     | 10        | third note    |
        | 4     | 13        | my added note |

    Scenario: Add a bunch of note with no notes currently present
        When I add a note "note 1"
        Then the response should be "Added note 1."
        When I add a note "note dos"
        Then the response should be "Added note 2."
        When I add a note "third note"
        Then the response should be "Added note 3."
        When I list notes
        # This is one down side of Gherkin - readability can suffer from checking
        # very long messages.
        Then the response should be "index | length | note\n1 | 6 | note 1\n2 | 8 | note dos\n3 | 10 | third note\n"
