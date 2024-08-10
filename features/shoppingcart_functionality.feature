Feature: Shopping Cart

  Scenario: User adds an item to their cart
    Given a user is on the product page
    When they click the "Add to Cart" button
    Then the item should be added to their cart

  Scenario: User views the items in their cart
    Given a user has items in their cart
    When they view the items in their cart
    Then they should see the items in their cart
