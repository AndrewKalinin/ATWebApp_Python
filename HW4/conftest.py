import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import pytest

with open("./testdata.yaml") as f:
	testdata = yaml.safe_load(f)
	browser = testdata['browser']

login = testdata['login']


@pytest.fixture(scope="session")
def browser():
	if browser == 'firefox':
		service = Service(executable_path=GeckoDriverManager().install())
		options = webdriver.FirefoxOptions()
		driver = webdriver.Firefox(service=service, options=options)
	else:
		service = Service(executable_path=ChromeDriverManager().install())
		options = webdriver.ChromeOptions()
		driver = webdriver.Chrome(service=service, options=options)
	yield driver
	driver.quit()


@pytest.fixture
def title_api():
	return "New post"


@pytest.fixture
def description_api():
	return "New description"


@pytest.fixture
def content_api():
	return "New content"

