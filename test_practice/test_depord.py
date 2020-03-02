import pytest
#import pytest_ordering
#@pytest.mark.dependency
@pytest.mark.run(order=2)
def test_login():
    print("in login")
#@pytest.mark.dependency(depends=["test_login"])
@pytest.mark.run(order=3)
def test_homepage():
    print("in homepage")

@pytest.mark.run(order=1)
def test_read():
    print("in read")
