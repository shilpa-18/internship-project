from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main page and Login')
def open_main_page(context):
    context.app.main_page.open_main_page()
    sleep(5)

@then('Input {email} and {password} to Login to the page')
def login_credentials(context, email, password):
    context.app.main_page.login_credentials(email, password)


@when('Open “Secondary” option at the left side menu')
def open_secondary(context):
    context.app.main_page.left_side_menu()
    sleep(5)

@then('Verify right page opens')
def correct_page(context):
    context.app.main_page.correct_page()
    sleep(5)

@then('Click on "Filters" at the top of the page')
def filters(context):
    context.app.main_page.filters()
    sleep(5)

@then('Filter the products by price range from {lower_amount} to {higher_amount} AED')
def filter_by_price(context, lower_amount, higher_amount):
    sleep(3)
    context.app.main_page.filter_by_price(lower_amount, higher_amount)
    sleep(3)

@then('Verify the price in all cards is inside the range')
def verify_price_range(context):
    context.app.main_page.verify_price_range(1200000, 2000000)
    sleep(5)

