from selenium.webdriver.common.by import By
import helper_methods as hm


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    # Elements
    accept_cookies_button = (By.CSS_SELECTOR, 'button[id="onetrust-accept-btn-handler"]')
    create_doodle = (By.CSS_SELECTOR, 'span[class="CreatePollMenu-createMenuLabel"]')

    def accept_cookies_policy(self):
        hm.click_on_element(self.driver, self.accept_cookies_button)

    def click_on_create_doodle(self):
        hm.click_on_element(self.driver, self.create_doodle)