from selenium.webdriver.common.by import By
import helper_methods as hm


class Doodle:
    def __init__(self, driver):
        self.driver = driver

    # elements of 1st step on poll
    title = (By.ID, 'd-pollTitle')
    continue_1st_step_button = (By.XPATH, '//section[@id="d-wizardGeneralInformationNavigationView"]//following-sibling::button[contains(@class, "d-nextButton")]')

    # elements of 2nd step on poll
    next_week_button = (By.CLASS_NAME, 'd-nextWeek')
    days_of_week = (By.XPATH, '//div[@class="d-dayHeaderContent"]/span[3]')
    continue_2nd_step_button = (By.XPATH, '//section[@id="d-wizardOptionsNavigationView"]//following-sibling::button[contains(@class, "d-nextButton")]')

    # elements of 3rd step on poll
    continue_3rd_step_button = (By.XPATH, '//section[@id="d-wizardSettingsNavigationView"]//following-sibling::button[contains(@class, "d-nextButton")]')

    # elements of 4th step on poll
    name_field = (By.ID, 'd-initiatorName')
    email_field = (By.ID, 'd-initiatorEmail')
    finish_button = (By.ID, 'd-persistPollButton')

    def select_days(self, days_list):
        days = hm.find_elements(self.driver, self.days_of_week, single_element=False)
        for day in days:
            if day.text in days_list:
                day.click()

    def create_doodle_1st_step(self, title):
        hm.enter_text(self.driver, self.title, title)
        hm.click_on_element(self.driver, self.continue_1st_step_button)

    def create_doodle_2nd_step(self, days_list, next_week=False):
        if next_week:
            hm.click_on_element(self.driver, self.next_week_button)

        self.select_days(days_list)
        hm.click_on_element(self.driver, self.continue_2nd_step_button)

    def create_doodle_3rd_step(self):
        hm.click_on_element(self.driver, self.continue_3rd_step_button)

    def create_doodle_4th_step(self, name, email):
        hm.enter_text(self.driver, self.name_field, name)
        hm.enter_text(self.driver, self.email_field, email)
        hm.click_on_element(self.driver, self.finish_button)







