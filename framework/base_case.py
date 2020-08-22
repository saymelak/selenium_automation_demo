from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.by import By


class BaseCase(unittest.TestCase):

    def raise_exc(self, val):
        raise KeyError(val)

    @classmethod
    def setUpClass(cls):
        global driver
        global wait
        global base_url

        base_url = "http://piassa.ca/test/"

        driver = webdriver.Chrome('lib/chromedriver')
        driver.get(base_url+'index.html')
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)

    @classmethod
    def tearDownClass(cls):
        """ Quite the browser """
        driver.quit()

    def Click(self, xpath):
        """ Click the specifies element """
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def Send(self, xpath, txt):
        """ Send the text to the specifies element/field """
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.send_keys(txt)

    def Select(self, xpath, txt):
        """ Send the text  to the dropdown field - this will select the specifies item"""
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.send_keys(txt)

    def Open(self, url):
        """ Navigates the current browser window to the specified page. """
        driver.get(url)
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
            print("Page is ready!")
        except TimeoutError:
            print("Loading took too much time!")

    def Navigate(self, xpath):
        """ Navigates the current browser window to the page using the specified menu item. """
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
            print("Page is ready!")
        except TimeoutError:
            print("Loading took too much time!")

    class Verify:
        def TextDisplayed(self, xpath, txt):
            """ Verify the specified txt is displayed """
            output_text = driver.find_element_by_xpath(xpath).text
            assert txt == output_text

        def TextNotDisplayed(self, xpath, txt):
            """ Verify the specified txt is not displayed """
            output_text = driver.find_element_by_xpath(xpath).text
            assert txt == output_text

        def ElementExists(self, xpath):
            """ Verify the specified element is displayed """
            count = driver.find_elements_by_xpath(xpath)
            assert len(count) == 1

        def ElementsExist(self, xpath):
            """ Verify the specified elements are displayed """
            count = driver.find_elements_by_xpath(xpath)
            assert len(count) > 0

        def PageTitle(self, title):
            """ Verify the title of the page """
            current_title = driver.title
            assert current_title == title

        def CanvasSize(self, xpath, width, height):
            w = driver.find_element_by_xpath(xpath).get_attribute("width")
            h = driver.find_element_by_xpath(xpath).get_attribute("height")
            print(w)
            print(h)
            assert str(width) == w
            assert str(height) == h
