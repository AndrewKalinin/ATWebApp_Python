import yaml

from pages.testpage import OperationHelper
from pages.post_page import OperationAddPost
from pages.contact_page import OperationContactUs
import logging

with open("./testdata.yaml") as f:
	testdata = yaml.safe_load(f)

login = testdata['login']
password = testdata['password']


def test_step1(browser):
	logging.info('test1 running')
	testpage = OperationHelper(browser)
	testpage.go_to_site()
	testpage.enter_login("test")
	testpage.enter_pass("test")
	testpage.click_login_button()
	assert testpage.get_error_text() == "401"


def test_step2(browser):
	logging.info('test2 running')
	testpage = OperationHelper(browser)
	testpage.enter_login(login)
	testpage.enter_pass(password)
	testpage.click_login_button()
	assert testpage.auth() == f"Hello, {login}"


def test_step3(browser):
	logging.info('test 3 running')
	testpage = OperationAddPost(browser)
	testpage.add_post()
	title = 'New title'
	testpage.post_context(title=title, description='New description', content='New content')
	assert title == testpage.check_post()


def test_step4(browser):
	logging.info('test 4 running')
	testpage = OperationAddPost(browser)
	testpage.go_to_site()
	testpage.add_post()
	title = 'New title2'
	testpage.post_context(title=title, description='New description')
	assert title == testpage.check_post()


def test_step5(browser):
	logging.info('test 5 running')
	testpage = OperationAddPost(browser)
	testpage.go_to_site()
	testpage.add_post()
	title = 'New title3'
	testpage.post_context(title=title, content='New content3')
	assert title == testpage.check_post()


def test_step6(browser):
	logging.info('test 6 running')
	testpage = OperationAddPost(browser)
	testpage.go_to_site()
	testpage.add_post()
	title = 'New title4'
	testpage.post_context(title=title)
	assert title == testpage.check_post()


def test_step7(browser):
	logging.info('test 7 running')
	testpage = OperationContactUs(browser)
	testpage.contact_click()
	testpage.fill_content_contact(name='My name', email='mymail@mail.com', content='hello')
	testpage.send_contact_info()
	assert 'Form successfully submitted' == testpage.search_alert().text

