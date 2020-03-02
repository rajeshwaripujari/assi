import pytest


@pytest.fixture(autouse=True)
def setup():
    print("in setup code")
    yield
    print("in teardown code")


def test_login():
    print("in login")


def test_logout():
    print("in logout")
