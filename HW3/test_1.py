import yaml
from testpage import OperationHelper
from post_page2 import OperationAddPost, OperationContactUs
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

login = testdata['username']
password = testdata['password']


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationHelper(browser)
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == f'Hello, {login}'


def test_step3(browser):
    logging.info("test 3 Starting")
    testpage = OperationAddPost(browser)
    testpage.add_post()
    title = 'Test new post'
    testpage.post_context(title=title, description='New description', content='New content')
    assert title == testpage.check_post()


def test_step4(browser):
    logging.info("test 4 Starting")
    testpage = OperationContactUs(browser)
    testpage.click_contact_button()
    testpage.Filling_in_fields(your_name='Andrey5', your_email='ak22@bk.ru', content='Hello!')
    alert_text = "Form successfully submitted"
    assert alert_text == testpage.check_alert()