import yaml

from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
from pages.BaseApp import parse_locators

ids = parse_locators('contact_locators.yaml')
	
	
class OperationContactUs(BasePage):
	def contact_click(self):
		self.click_button(ids['LOCATOR_CONTACT_BTN'])
		# logging.info('search and click button "Contact"')
		# return self.find_element(ContactUsLocators.LOCATOR_CONTACT_BTN).click()
	
	def fill_content_contact(self, name=None, email=None, content=None):
		self.enter_text_into_field(ids['LOCATOR_CONTACT_NAME'], name)
		# name_field = self.find_element(ContactUsLocators.LOCATOR_CONTACT_NAME)
		# name_field.clear()
		# if name:
		# 	logging.info('add name')
		# 	name_field.send_keys(name)
		self.enter_text_into_field(ids['LOCATOR_CONTACT_EMAIL'], email)
		# email_field = self.find_element(ContactUsLocators.LOCATOR_CONTACT_EMAIL)
		# email_field.clear()
		# if email:
		# 	logging.info('add email')
		# 	email_field.send_keys(email)
		self.enter_text_into_field(ids['LOCATOR_CONTACT_CONTENT'], content)
		# content_field = self.find_element(ContactUsLocators.LOCATOR_CONTACT_CONTENT)
		# content_field.clear()
		# if content:
		# 	logging.info('add content')
		# 	content_field.send_keys(content)
		
	def send_contact_info(self):
		# logging.info('Send info to contact us')
		# return self.find_element(ContactUsLocators.LOCATOR_CONTACT_SEND_BTN).click()
		self.click_button(ids['LOCATOR_CONTACT_SEND_BTN'])
	