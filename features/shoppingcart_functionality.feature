Feature: Add to Cart
Scenario: User adds an item to their cart.

    Given a user is viewing a product page for a laptop,
    When they click the "Add to Cart" button,
    Then the item should be added to their shopping cart and the cart icon should display the updated number of items.

Scenario: User views the items in their cart.

    Given a user has added items to their cart,
    When they click on the cart icon,
    Then they should see a detailed list of all items in their cart, including prices and quantities.