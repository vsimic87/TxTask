from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def find_elements(driver, locator, timeout=5, single_element=True):
    """
    Method find an element/elements depending on single_element param and
    returns element/elements for given locator
    """
    try:
        if single_element:
            find_function = EC.presence_of_element_located
        else:
            find_function = EC.presence_of_all_elements_located

        elements = WebDriverWait(driver, timeout).until(find_function(locator))

        # elements = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)) if single_element else WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))
    except (NoSuchElementException, TimeoutException):
        return None
    return elements


def is_element_displayed_by_locator(driver, locator, by=By.ID):
    """
    Method verify visibility of element for given locator and
    returns True if element is visible, otherwise False
    """
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        return False
    return element.is_displayed()


def click_on_element(driver, locator, timeout=5):
    element = find_elements(driver, locator, timeout)
    return element.click()


def wait_until_element_is_visible_by_id(driver, locator, timeout=5, by=By.ID,
                                        msg="Element located by '{}' with locator '{}' not found within {} seconds"):
    """
    returns True if element is visible within timeout, otherwise False
    """
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)),
                                         msg.format(by, locator, timeout))


def enter_text(driver, locator, text, timeout=5):
    """
    Method calling find_elements method and inserts value(text) for returned element
    """
    element = find_elements(driver, locator, timeout)
    element.send_keys(text)




