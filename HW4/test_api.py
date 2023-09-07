from module_api import post, auth


def test_step1():
	assert auth() == 200, "TEST1 FAIL"


def test_step2(title_api, description_api, content_api):
	assert post(title_api, description_api, content_api) == description_api, "TEST2 FAIL"
	
