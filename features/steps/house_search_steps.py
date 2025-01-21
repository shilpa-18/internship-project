from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main page and Login')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Open “Secondary” option at the left side menu')
def open_secondary(context):
    context.app.main_page.left_side_menu()

@then('Verify right page opens')
def correct_page(context):
    context.app.main_page.correct_page()

@then('Open "Filters" and input the {lower_price} and {higher_price}')
def open_filters(context, lower_price, higher_price):
    context.app.main_page.open_filters(int(lower_price), int(higher_price))

@then('Verify the price in all cards is inside the range')
def verify_price_inside_range(context):
