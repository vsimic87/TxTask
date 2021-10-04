from BaseTest import BaseTest
from pages.CreateDoodle import Doodle
from pages.Poll import Poll
from pages.Homepage import Homepage
from pages.PollConfirmation import PollConfirmation
from data.CreateDoodleData import create_doodle_and_response_on_poll_data as data


class TestCreateDoodlePage(BaseTest):
    def test_create_doodle_and_response_on_poll(self):

        # Initialing the Homepage page
        page_home = Homepage(self.driver)

        # Accept privacy policy for cookies
        page_home.accept_cookies_policy()

        # Click to create doodle button
        page_home.click_on_create_doodle()

        # Initialing the Doodle page
        page_doodle = Doodle(self.driver)

        # Fill the necessary data on each step of Doodle creation
        page_doodle.create_doodle_1st_step(data['title'])
        page_doodle.create_doodle_2nd_step(data['working_days'], next_week=True)
        page_doodle.create_doodle_3rd_step()
        page_doodle.create_doodle_4th_step(data['name'], data['email'])

        # Initialing the Poll page
        page_poll = Poll(self.driver)
        # Selecting 3 options and send response
        page_poll.select_option(0)
        page_poll.select_option(3)
        page_poll.select_option(4)
        page_poll.click_on_send_button()

        # Initialing the PollConfirmation page
        page_poll_confirmation = PollConfirmation(self.driver)
        # Wait for page to load
        page_poll_confirmation.wait_confirmation_page_to_load()
        # Verify user successfully voted
        alert_text = page_poll_confirmation.get_alert_text()
        self.assertEqual('You have successfully voted', alert_text, "Vote wasn't successful")
