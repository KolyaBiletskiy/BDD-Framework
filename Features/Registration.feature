Feature: verify registration functionality

  @smoke @sanity
  Scenario: Registration with valid data
    Given User is on registration page
    When user enters "<name>"
    And user enters email id
    And user enters password
    And user clock on signup button
    Then user should be registered successfully

  @major
  Scenario: Registration with duplicated username
    Given User is on registration page
    When user enters username
    And user enters username
    And user enters password
    And user clock on signup button
    Then user should not be registered successfully

