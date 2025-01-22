from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main page and Login')
def open_main_page(context):
    context.app.main_page.open_main_page()
    sleep(5)

@then('Input {email} and {password} to Login to the page')
def login_credentials(context, email, password):
    sleep(10)
    context.app.main_page.login_credentials(email, password)

@when('Open “Secondary” option at the left side menu')
def open_secondary(context):
    context.app.main_page.left_side_menu()
    sleep(5)

@then('Verify right page opens')
def correct_page(context):
    context.app.main_page.correct_page()
    sleep(5)

@then('Open "Filters" and input the {lower_price} and {higher_price}')
def open_filters(context, lower_price, higher_price):
    context.app.main_page.open_filters(int(lower_price), int(higher_price))
    sleep(5)

@then('Verify the price in all cards is inside the range')
def verify_price_inside_range(context):
    context.app.main_page.verify_price_inside_range()
    sleep(5)