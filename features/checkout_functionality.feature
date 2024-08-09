Feature: Complete Purchase
Scenario: User proceeds to checkout.

    Given a user has items in their cart,
    When they click on the "Proceed to Checkout" button,
    Then they should be directed to the checkout page where they can review their order and enter shipping and payment information.

Scenario: User completes their purchase.

    Given a user is on the checkout page with all required fields filled out,
    When they click the "Place Your Order" button,
    Then their order should be successfully placed and they should see an order confirmation page.