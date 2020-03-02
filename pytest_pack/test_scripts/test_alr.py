import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType

chromePath = r"C:\Users\Basavarajeshwri\PycharmProjects\ptest\pytest_pack\driver\chromedriver.exe"
driver = None


@pytest.fixture(autouse=True)
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path=chromePath)
    driver.implicitly_wait(6)
    driver.get("https://demo.actitime.com/login.do")
    yield
    driver.close()
    print("close")




def test_actitime():
    driver.find_element_by_xpath("//input[@id='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='pwd']").send_keys("manager")
    driver.find_element_by_xpath("//div[text()='Login ']").click()
    import time
    time.sleep(6)
    allure.attach(driver.get_screenshot_as_png(), name="actitime", attachment_type=AttachmentType.PNG)
