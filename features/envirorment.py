

def before_all(context):
    print("welcome ")
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")