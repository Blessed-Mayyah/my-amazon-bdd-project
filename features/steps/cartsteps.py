from behave import given, when, then

@given(u'a user is on the product page')
def step_impl(context):
    # Navigate to a product page
    context.browser.get('http://example.com/product-page')

@when(u'they click the "Add to Cart" button')
def step_impl(context):
    # Simulate clicking the "Add to Cart" button
    add_to_cart_button = context.browser.find_element_by_id('add-to-cart')
    add_to_cart_button.click()

@then(u'the item should be added to their cart')
def step_impl(context):
    # Verify the item is added to the cart
    cart_icon = context.browser.find_element_by_id('cart-icon')
    cart_icon.click()
    cart_items = context.browser.find_elements_by_class_name('cart-item')
    assert len(cart_items) > 0, "No items found in the cart"

@given(u'a user has items in their cart')
def step_impl(context):
    # Ensure items are added to the cart
    context.browser.get('http://example.com/product-page')
    add_to_cart_button = context.browser.find_element_by_id('add-to-cart')
    add_to_cart_button.click()

@when(u'they view the items in their cart')
def step_impl(context):
    # Navigate to the cart page
    context.browser.get('http://example.com/cart')

@then(u'they should see the items in their cart')
def step_impl(context):
    # Verify items are visible in the cart
    cart_items = context.browser.find_elements_by_class_name('cart-item')
    assert len(cart_items) > 0, "No items found in the cart"
