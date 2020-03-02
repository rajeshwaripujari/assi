import pytest
@pytest.fixture(autouse=True)
def setup(request):
    print("in setup code")
    print("data in request",request)

def teardown():
    print("in teardown code")
def test_login():
    print("in login function")
def test_logout():
    print("in logout function")