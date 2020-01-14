Feature: List notes
    As a user
    I want to list all my notes
    So that I can reflect on my previous notes

    Scenario: List without any notes present
        When I list notes
        Then the response should be empty

    Scenario: List some notes
        Given that there are notes:
        | first note    |
        | second note   |
        | third note    |
        When I list notes
        Then the response should be:
        | first note    |
        | second note   |
        | third note    |
