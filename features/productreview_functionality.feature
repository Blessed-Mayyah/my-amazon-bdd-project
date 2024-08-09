Feature: Submit Product Review
Scenario: User submits a review for a purchased product.

    Given a user has purchased a product,
    When they navigate to the product page and click "Write a Review",
    Then they should be able to enter their review, select a star rating, and submit it.

Scenario: User views reviews for a product.

    Given a user is viewing a product page,
    When they scroll to the reviews section,
    Then they should see a list of reviews and ratings submitted by other custom