from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def before_all(context):
    print("welcome")
    # Correct way: Wrap path in Service, then pass to webdriver.Chrome
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()



#
# def after_all(context):
#     print("after_all")
#     if hasattr(context, "driver"):
#         context.driver.quit()