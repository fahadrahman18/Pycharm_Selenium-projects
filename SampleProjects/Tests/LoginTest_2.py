from selenium import webdriver
import time
import unittest
import HTMLTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProjects.Pages.loginpage import LoginPage
from SampleProjects.Pages.homePage import HomePage

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/selenium_try1/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)   #driver is important, in constructor argument we are taking to pas driver instance
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.login_click()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        homepage.click_logout_link()





        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()
        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='C:/Users/User/PycharmProjects/selenium_try1/Reporting'))

