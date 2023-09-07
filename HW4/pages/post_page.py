import time

import yaml
from pages.BaseApp import BasePage, parse_locators
from selenium.webdriver.common.by import By
import logging


ids = parse_locators('post_locators.yaml')


class OperationAddPost(BasePage):
	def add_post(self):
		self.click_button(ids['LOCATOR_ADD_POST'])
	
	# logging.info('Add post')
	# add_post_btn = self.find_element(AddPostLocators.LOCATOR_ADD_POST)
	# add_post_btn.click()
	
	def post_context(self, title=None, description=None, content=None):
		self.enter_text_into_field(ids['LOCATOR_TITLE'], title)
		self.enter_text_into_field(ids['LOCATOR_DESCRIPTION'], description)
		self.enter_text_into_field(ids['LOCATOR_CONTENT'], content)
		self.click_button(ids['LOCATOR_CREATE_POST'])
	
	# title_field = self.find_element(AddPostLocators.LOCATOR_TITLE)
	# title_field.clear()
	# if title:
	# 	logging.info(f'fill post: {title}')
	# 	title_field.send_keys(title)
	# description_field = self.find_element(AddPostLocators.LOCATOR_DESCRIPTION)
	# description_field.clear()
	# if description:
	# 	logging.info(f'fill post: {description}')
	# 	description_field.send_keys(description)
	# content_field = self.find_element(AddPostLocators.LOCATOR_CONTENT)
	# content_field.clear()
	# if content:
	# 	logging.info(f'fill post: {content}')
	# 	content_field.send_keys(content)
	# logging.info(f'button click')
	# btn = self.find_element(AddPostLocators.LOCATOR_CREATE_POST)
	# btn.click()
	
	def check_post(self):
		# logging.info("checking new post...")
		time.sleep(1)
		return self.get_text_from_element(ids['LOCATOR_CHECK_POST'])
	
	# self.find_element(AddPostLocators.LOCATOR_CHECK_POST).text
