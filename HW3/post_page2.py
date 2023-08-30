import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class AddPostLocators:
    LOCATOR_ADD_POST = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_TITLE = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_DESCRIPTION = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CONTENT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_CREATE_POST = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_CHECK_POST = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')


class OperationAddPost(BasePage):
    def add_post(self):
        logging.info("Creating a new post")
        add_post_btn = self.find_element(AddPostLocators.LOCATOR_ADD_POST)
        add_post_btn.click()

    def post_context(self, title=None, description=None, content=None):
        logging.info("Filling in field: title")
        title_field = self.find_element(AddPostLocators.LOCATOR_TITLE)
        title_field.send_keys(title)
        logging.info("Filling in field: description")
        description_field = self.find_element(AddPostLocators.LOCATOR_DESCRIPTION)
        description_field.send_keys(description)
        logging.info("Filling in field: content")
        content_field = self.find_element(AddPostLocators.LOCATOR_CONTENT)
        content_field.send_keys(content)
        btn = self.find_element(AddPostLocators.LOCATOR_CREATE_POST)
        btn.click()
        time.sleep(2)

    def check_post(self):
        logging.info("Checking new post...")
        return self.find_element(AddPostLocators.LOCATOR_CHECK_POST).text


class ContactUsLocators:
    LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_YOUR_NAME = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_YOUR_EMAIL = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, '#contact > div.submit > button > span')


class OperationContactUs(BasePage):
    def click_contact_button(self):
        logging.info("Click contact button")
        return self.find_element(ContactUsLocators.LOCATOR_CONTACT_BTN).click()

    def Filling_in_fields(self, your_name=None, your_email=None, content=None):
        logging.info("Filling in field: Your name")
        your_name_field = self.find_element(ContactUsLocators.LOCATOR_YOUR_NAME)
        your_name_field.send_keys(your_name)
        logging.info("Filling in field: Your email")
        your_email_field = self.find_element(ContactUsLocators.LOCATOR_YOUR_EMAIL)
        your_email_field.send_keys(your_email)
        logging.info("Filling in field: Content")
        content_field = self.find_element(ContactUsLocators.LOCATOR_CONTENT)
        content_field.send_keys(content)
        logging.info("Click 'CONTACT US' button")
        btn = self.find_element(ContactUsLocators.LOCATOR_CONTACT_US_BTN)
        time.sleep(1)
        btn.click()
        time.sleep(1)

    def check_alert(self):
        logging.info("Appearance pop-up alert")
        return self.get_alert().text