import pytest
@pytest.fixture(params=["chrome","firefox"],autouse=True)
def setup(request):
    print("open",request.param)
    yield
    print("close",request.param)

'''@pytest.fixture(scope='function',autouse=True)
def function_setup():
    print("in setup code function")
    yield
    print("in teardown code function")
@pytest.fixture(scope='class',autouse=True)
def class_setup():
    print("in setup code class")
    yield
    print("in teardown code class")
@pytest.fixture(scope='session',autouse=True)
def session_setup():
    print("in setup code session")
    yield
    print("in teardown code session")
@pytest.fixture(scope='module',autouse=True)
def module_setup():
    print("in setup code module")
    yield
    print("in teardown code module")
'''
def test_login():
    print("in login")
def test_logout():
    print("in logout")