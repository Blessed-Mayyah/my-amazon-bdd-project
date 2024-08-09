Feature: Login and Profile Management
Scenario 1: User logs into their account.

    Given a user is on the Amazon homepage,
    When they click the "Sign In" button and enter valid login credentials,
    Then they should be successfully logged in and redirected to their account dashboard.

Scenario 2: User updates their profile information.

    Given a user is logged into their account,
    When they navigate to the "Your Account" section and update their shipping address,
    Then the new address should be saved and reflected in their profile.