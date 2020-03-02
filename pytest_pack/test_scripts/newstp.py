import pytest
#pytestmark = pytest.mark.usefixtures("setup")

@pytest.fixture()
def setUp():
    print("in setup function")


def test_login(setUp):
    print("in login function")

def test_logout():
    print("in logout function")


