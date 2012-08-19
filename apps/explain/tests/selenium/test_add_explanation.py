from django.test import LiveServerTestCase
from selenium import webdriver

class NewItemExplTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_explanation(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("search").send_keys("reddit")
        self.browser.find_element_by_id("search-button").click()
        self.browser.find_element_by_id("id_name").send_keys("reddit")
        self.browser.find_element_by_id("id_explanation_set-0-body").send_keys("Reddit is a fun place to share links.")
        self.browser.find_element_by_id('save-item').click()
        self.browser.find_element_by_link_text("Submit a New Explanation").click()
        self.browser.find_element_by_id("id_body").send_keys("this is my new explanation")
        self.browser.find_element_by_id("add-explanation").click()

