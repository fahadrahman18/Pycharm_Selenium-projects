from selenium import webdriver
import unittest
import HTMLTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")   #cls is variable
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")                                          #self is variable
        self.driver.find_element_by_name("q").send_keys("Automation testing")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)

    def test_search_testing(self):
        self.driver.get("https://google.com")                                          #self is variable
        self.driver.find_element_by_name("q").send_keys("testing")
        self.driver.find_element_by_name("btnK1").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ =='__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='C:/Users/User/PycharmProjects/selenium_try1/Reporting'),verbosity=2)








