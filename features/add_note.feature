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
        # Gherkin is not immune to readability issues and in fact has a few of its own:
        When I add a note "a very long, obnoxious, really hard to read, falling off the edge of the screen, have to scroll a long way to see it all, you have to wonder who thought this was a good idea note"
        Then the response should be "Added note 4."
        When I list notes
        # This is one down side of Gherkin - readability can suffer from checking
        # very long messages.
        Then the response should be:
        | index | length    | note          |
        | 1     | 6         | note 1        |
        | 2     | 8         | note dos      |
        | 3     | 10        | third note    |
        | 4     | 178       | a very long, obnoxious, really hard to read, falling off the edge of the screen, have to scroll a long way to see it all, you have to wonder who thought this was a good idea note |
