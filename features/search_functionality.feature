
Feature: Search Functionality

  Scenario: User searches for a specific product by name
    Given a user is on Amazon homepage
    When they enter "laptop" into the search bar and click the search button
    Then they should see a list of laptops matching the search term

  Scenario: User uses filters to narrow down search results
    Given a user has searched for "laptop"
    When they apply filters such as brand and price range
    Then the search results should update to show only laptops that meet the specified criteria

