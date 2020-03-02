import pytest
pytestmark = pytest.mark.usefixtures("setup")

@pytest.fixture()
def setup():
    print("in setup function")


def test_login():
    print("in login function")


def test_logout():
    print("in logout function")
