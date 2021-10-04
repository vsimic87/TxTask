from selenium.webdriver.common.by import By
import helper_methods as hm


class Poll:
    def __init__(self, driver):
        self.driver = driver

    # Elements
    send_button = (By.CSS_SELECTOR, '#d-pollActionBarView .d-send')

    def select_option(self, option):
        choice = (By.CSS_SELECTOR, 'div[class*="d-participantPreference"] label[for^="d-participantPreference"][for$="-{}"] g[class="d-defaultCheckmark"]'.format(option))
        hm.click_on_element(self.driver, choice)

    def click_on_send_button(self):
        hm.click_on_element(self.driver, self.send_button)
