from django.test import LiveServerTestCase
from selenium import webdriver
from django.core.urlresolvers import reverse

class LoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get(self.live_server_url)
        self.browser.get(self.live_server_url + "/accounts/registration/")
        self.browser.find_element_by_id("id_username").send_keys("user")
        self.browser.find_element_by_id("id_password").send_keys("mypassword")
        self.browser.find_element_by_id("register-button").click()
        self.browser.get(self.live_server_url + reverse("django.contrib.auth.views.logout"))
        self.browser.get(self.live_server_url + reverse("django.contrib.auth.views.login"))
        self.browser.find_element_by_id("id_username").send_keys("user")
        self.browser.find_element_by_id("id_password").send_keys("mypassword")
        self.browser.find_element_by_id("login-button").click()
