import time
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
login = testdata['username']
password = testdata['password']


def test_step1(sel_1, x_selector2,btn_selector, x_selector3, result):
    input1 = site.find_element("xpath", sel_1)
    input1.clear()
    input1.send_keys("test")

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("test")

    btn = site.find_element("css", btn_selector)
    btn.click()

    err_label = site.find_element("xpath", x_selector3)
    res = err_label.text
    assert res == result


def test_step2(sel_1, x_selector2, btn_selector, auth, result2):
    input1 = site.find_element("xpath", sel_1)
    input1.clear()
    input1.send_keys(login)

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(password)

    btn = site.find_element("css", btn_selector)
    btn.click()

    auth = site.find_element('xpath', auth)
    res = auth.text
    assert res == result2


def test_step3(create_btn_selector, title, description, content, create, get_title):
    btn = site.find_element("css", create_btn_selector)

    btn.click()
    input_title = site.find_element("xpath", title)
    input_title.send_keys("New post")
    input_description = site.find_element("xpath", description)
    input_description.send_keys("New Description")
    input_content = site.find_element("xpath", content)
    input_content.send_keys("Создание поста с использованием Selenium WebDriver")
    btn = site.find_element("xpath", create)
    time.sleep(2)
    btn.click()
    time.sleep(3)
    title = site.find_element("xpath", get_title)
    res = title.text
    site.close()
    assert res == "New post"