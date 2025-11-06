Feature: Find book by description
  Scenario: Find The Hobbit by mentioning dragons
    Given the BookSeeker database is loaded
    When I search for "a hobbit and a dragon"
    Then the top result should contain "The Hobbit"
