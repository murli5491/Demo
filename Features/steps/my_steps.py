from behave import *
from behave.api.pending_step import StepNotImplementedError
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


@given("launch the browser")
def step_impl(context):
   context.driver =Chrome()


@when(u'open the orange HRM')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'verify login button is displayed')
def step_impl(context):
    try:
        element = context.driver.find_element(By.NAME, "username")  # Username field
        if element.is_displayed():
            print("✅ Username field is displayed!")
        else:
            print("⚠ Username field exists but is not visible.")
    except NoSuchElementException:
        print("❌ Username field not found.")
@when(u'Enter UserName "{username}" And EnterPassword "{password}"')
def step_impl(context, username, password):
    username_field = context.driver.find_element(By.NAME, "username")
    username_field.clear()
    username_field.send_keys(username)

    password_field = context.driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(password)

@when("Click on login button")
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "//*[@type='submit']")
    login_button.click()


@then("close browser")
def step_impl(context):
    context.driver.quit()

