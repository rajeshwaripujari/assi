import pytest


@pytest.fixture()
def setup():
    print("in setup function")


def test_login(setup):
    print("in login function")


def test_logout(setup):
    print("in logout function")
