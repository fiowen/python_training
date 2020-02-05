# Generated by Selenium IDE
import pytest
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginandaddanewgroup(unittest.TestCase):
    def setup_method(self, method):
        self.wd = webdriver.Chrome()
        self.vars = {}

    def test_login_and_add_new_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://192.168.64.2/addressbook/")
        wd.set_window_size(1280, 731)

    def login(self, wd):
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value=\'Login\']").click()

    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys("first_new_group")
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys("header")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys("footer")
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def return_to_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def teardown_method(self, method):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()

