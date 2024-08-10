Feature: Product Reviews

  Scenario: User views reviews for a product
    Given a user is on the product page
    When they scroll to the reviews section
    Then they should see reviews for the product
