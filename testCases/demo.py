import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from appium_flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import MobileKeys

desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.example.real_state2",
    "appActivity": ".MainActivity",
    "app": "C:\\Users\\kazia\\AppData\\Local\\Android\\Sdk\\platform-tools\\test.apk"
}
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
# driver.implicitly_wait(30)
time.sleep(5)

try:
    name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget" \
           ".FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/" \
           "android.widget.ImageView[2]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=name,
    )
    element.click()
    element.send_keys('Kazi Saad')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    email = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android" \
            ".widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view." \
            "View/android.widget.ImageView[3]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=email,
    )
    element.click()
    element.send_keys('kazi.arisaftech@gmail.com')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    password = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android." \
               "widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android." \
               "view.View/android.widget.EditText[1]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=password,
    )
    element.click()
    element.send_keys('pass1234')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    confirmPassword = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                      "android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view." \
                      "View/android.view.View/android.widget.EditText[2]"
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=confirmPassword,
    )
    element.click()
    element.send_keys('pass1234')
    time.sleep(2)
    driver.press_keycode(66)
    time.sleep(5)

    signIn = '//android.widget.Button[@content-desc="Sign In"]'
    element = driver.find_element(
        by=AppiumBy.XPATH,
        value=signIn,
    )
    element.click()
    time.sleep(10)
    print('Sign In: Successful ✔')
except Exception as e:
    print('Sign In: Failed! 👎')
    print(f"Error from Sign In: {e}")

    driver.close()
