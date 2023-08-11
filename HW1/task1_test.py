from task1 import auth_user, posts_another_user, create_post


def test_step1():
    assert auth_user() == 200, "test1 FAIL"


def test_step2():
    assert posts_another_user() == 200, "test2 FAIL"


def test_step3():
    assert create_post() == 'song', "test3 FAIL"