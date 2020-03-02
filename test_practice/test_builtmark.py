import pytest
#pytestmark = pytest.mark.skip(reason="skip the entire module")
#@pytest.mark.skip
#title="abc"
#pytest.mark.skipif("abc"==title,reason="matched")
@pytest.mark.parametrize("args1,args2",[(11,22),(33,44)])
def test_logout(args1,args2):
    print("in logout",args1,args2)
class Test_logout():
    def test_display1(self):
        print("in display1")
    #@pytest.mark.skip(reason="not created")
    def test_read(self):
        print("in read1 ")

@pytest.mark.raj
def test_read():
    print("in read")