import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from appium_flutter_finder import FlutterElement, FlutterFinder

desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.example.init_test",
    "appActivity": ".MainActivity",
    "app": "C:\\Users\\kazia\\AppData\\Local\\Android\\Sdk\\platform-tools\\app-release.apk"
}
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
driver.implicitly_wait(30)


# # Define a function to check if the session is active
# def is_session_active(Driver):
#     try:
#         var = Driver.title  # This is just an example, you can use any method or property to check the session
#         return True
#
#     except NoSuchElementException:
#         return False


try:
    name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
           "widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android." \
           "widget.Button"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=name,
    )
    element.click()

    # Check if the session is still active before proceeding
    # if is_session_active(driver):
    time.sleep(60)
    print("successful")
    # else:
    #     print("Session is no longer active.")
except Exception as e:
    print(f"this is the error: {e}")
