import pytest


@pytest.fixture(autouse=True)
def setup():
    print("in setup function")


def test_login():
    print("in login function")


def test_logout():
    print("in logout function")
