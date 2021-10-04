from selenium.webdriver.common.by import By
import helper_methods as hm


class PollConfirmation:
    def __init__(self, driver):
        self.driver = driver

    # Elements
    confirmation_section = (By.ID, 'd-participationConfirmationView')
    alert_success = (By.CLASS_NAME, 'd-premiumHookNag')

    def wait_confirmation_page_to_load(self):
        hm.wait_until_element_is_visible_by_id(self.driver, self.confirmation_section[1])

    def get_alert_text(self):
        element = hm.find_elements(self.driver, self.alert_success)
        return element.text

