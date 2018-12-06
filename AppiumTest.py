import os
import unittest
from appium import webdriver
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6' # Chabge
        desired_caps['deviceName'] = '26e5ca52' # Change
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        desired_caps['appActivity'] = 'com.ss.android.article.news.activity.MainActivity'
        desired_caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def tearDown(self):
    #     self.driver.quit()

    def test_add_contacts(self):
        time.sleep(3)
        print("Hello")
        self.driver.implicitly_wait(10)
        el = self.driver.find_elements_by_id("com.ss.android.article.news:id/cit")
        print(len(el))
        for i in range(len(el)):
            print(el[i])
        el[1].click()