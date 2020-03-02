import pytest


@pytest.mark.skip
def test_login():
    print(" in test login")


class TestLogout():
    def test_display1(self):
        print("in display1")

    @pytest.mark.skip(reason="not created")
    def test_read1(self):
        print("in test read1")
