from behave import *
from behave.api.pending_step import StepNotImplementedError
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@given("launch the browser")
def step_impl(context):
    context.driver = Chrome()


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


@then("close browser")
def step_impl(context):
    context.driver.quit()


@when(u'Enter UserName "{username}" And EnterPassword "{password}"')
def step_impl(context, username, password):
    wait = WebDriverWait(context.driver, 10)

    # Wait for username field
    username_field = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.clear()
    username_field.send_keys(username)

    # Wait for password field
    password_field = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.clear()
    password_field.send_keys(password)


@when(u'click on login button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Wait for username field
    username_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@type='submit']"))
    )
    username_field.click()


@then(u'user must successfully login to the dashboard page')
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        # Wait for the dashboard banner to be visible
        username_field = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='oxd-brand-banner']"))
        )
    except:
        context.driver.close()
        assert False, "test  failed"

    if username_field.is_displayed() == True:
        context.driver.close()
        assert True, "test  passed"


@then(u'click on admin button')
def step_impl(context):
    try:
        element = context.driver.find_element(By.XPATH, "//span[text()='Admin']")  # Username field
        if element.is_displayed():
            print("✅ Username field is displayed!")
        else:
            print("⚠ Username field exists but is not visible.")
    except NoSuchElementException:
        print("❌ Username field not found.")

