from django.test import LiveServerTestCase
from selenium import webdriver

class NewItemTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_new_item(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("search").send_keys("reddit")
        self.browser.find_element_by_id("search-button").click()
        self.browser.find_element_by_id("id_name").send_keys("reddit")
        self.browser.find_element_by_id("id_type").send_keys("http://www.reddit.com/")
        self.browser.find_element_by_id("id_explanation_set-0-body").send_keys("Reddit is a fun place to share links.")
        self.browser.find_element_by_class_name("btn").click()
