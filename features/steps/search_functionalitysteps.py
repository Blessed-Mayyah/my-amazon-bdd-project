from behave import given, when, then

@given(u'the user is on Amazon homepage')
def step_impl(context):
    # Setup code to navigate to the Amazon homepage
    raise NotImplementedError(u'STEP: Given the user is on the Amazon homepage')

@when(u'the user enters "laptop" into the search bar and clicks the search button')
def step_impl(context):
    # Code to enter "laptop" into the search bar and click search
    context.result = "Search results for laptops"

@then(u'the user should see a list of laptops matching the search term')
def step_impl(context):
    # Code to verify that search results include a list of laptops
    raise NotImplementedError(u'STEP: Then the user should see a list of laptops matching the search term')

#SCENARIO TWO
@given(u'the user has searched for "laptop"')
def step_impl(context):
    # Code to ensure the user has performed a search for "laptop"
    raise NotImplementedError(u'STEP: Given the user has searched for "laptop"')

@when(u'the user applies filters such as brand and price range')
def step_impl(context):
    # Code to apply filters like brand and price range
    context.result = "Filtered search results"

@then(u'the search results should update to show only laptops that meet the specified criteria')
def step_impl(context):
    # Code to verify that search results match the applied filters
    raise NotImplementedError(u'STEP: Then the search results should update to show only laptops that meet the specified criteria')
