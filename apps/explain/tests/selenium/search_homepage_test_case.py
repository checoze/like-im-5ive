from django.test import LiveServerTestCase
from selenium import webdriver

class SearchHomePageTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_search_home_page(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("search").send_keys("reddit")
        self.browser.find_element_by_id("search-button").click()
