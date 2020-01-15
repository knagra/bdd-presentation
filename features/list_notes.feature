Feature: List notes
    As a user
    I want to list all my notes
    So that I can reflect on my previous notes

    Scenario: List without any notes present
        When I list notes
        Then the response should be:
        | index | length    | note  |

    Scenario: List some notes
        Given that there are notes:
        | note          |
        | first note    |
        | second note   |
        | third note    |
        When I list notes
        Then the response should be:
        | index | length    | note          |
        | 1     | 10        | first note    |
        | 2     | 11        | second note   |
        | 3     | 10        | third note    |
