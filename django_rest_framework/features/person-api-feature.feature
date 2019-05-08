Feature: People Management API

    Scenario:  Valid Create Person Resource using POST
        Given a valid person
        When I call POST for the people API
        Then a person resource will be created

    Scenario: Invalid Create Person Resource using POST - Missing First Name
        Given a person missing first name
        When I call POST for the people API
        Then a bad request response is recieved

    Scenario: Invalid Create Person Resource using POST - Missing Last Name
        Given a person missing last name
        When I call POST for the people API
        Then a bad request response is recieved

    Scenario: Invalid Create Person Resource using POST - Missing Age
        Given a person missing age
        When I call POST for the people API
        Then a bad request response is recieved