from SampleProjects.Locators.locators import Locators
class LoginPage():

    def __init__(self, driver):      #constructor
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id                       #import locators using locators class program
        self.password_textbox_id = "txtPassword"                                      ##self passwordobject_typetextbox_locatorid
        self.login_button_id     = "btnLogin"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()                #good practice is clear the text before entering value
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def login_click(self):
        self.driver.find_element_by_id(self.login_button_id).click()

