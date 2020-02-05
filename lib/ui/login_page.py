from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def get_internal_user_button(self):
        try:
            return self.driver.find_element_by_xpath("//button[contains(text(),'Western Digital Internal User')]")
        except:
            return None

    def get_customer_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//button[contains(text(),'Customer Login')]")
        except:
            return None

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_id('usernameInput')
        except:
            return None

    def get_password_texbox(self):
        try:
            return self.driver.find_element_by_id('passwordInput')
        except:
            return None
    def get_login_button(self):
        try:
            return self.driver.find_element_by_partial_link_text("Login")
        except:
            return None
    def get_username_require_msg(self):
        try:
            return self.driver.find_element_by_partial_link_text('Username is required')
        except:
            return None
    def wait_for_login_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_customer_login_button()))




