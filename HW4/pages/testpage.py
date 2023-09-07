from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml
from pages.BaseApp import parse_locators

ids = parse_locators('locators.yaml')


class OperationHelper(BasePage):
	
	def enter_login(self, word):
		self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, "login_field")
	
	def enter_pass(self, word):
		self.enter_text_into_field(ids["LOCATOR_PASS_FIELD"], word, 'pass_field')
	
	# logging.info(f"Sent {word} to element {TestSearchLocators.ids['LOCATOR_PASS_FIELD'][1]}")
	# login_field = self.find_element(TestSearchLocators.ids['LOCATOR_PASS_FIELD'])
	# login_field.clear()
	# login_field.send_keys(word)
	
	def click_login_button(self):
		self.click_button(ids['LOCATOR_LOGIN_BTN'], " login_btn")
	
	def get_error_text(self):
		return self.get_text_from_element(ids['LOCATOR_ERROR_FIELD'], "login_error")
	
	def auth(self):
		return self.find_element(ids['LOCATOR_AUTH']).text
