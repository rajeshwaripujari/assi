from selenium import webdriver
from datadrvn.dataxl import XlData as xl
filepath = r"C:\Users\Basavarajeshwri\PycharmProjects\ptest\datadrvn\data.xlsx"
sheetname = r"Sheet1"
chromePath = r"C:\Users\Basavarajeshwri\PycharmProjects\ptest\pytest_pack\driver\chromedriver.exe"
def login():
    obj = xl()
    row = obj.sheetObj(filepath,sheetname)[2]
    for i in range(2,row+1):
        driver = webdriver.Chrome(executable_path=chromePath)
        driver.get("https://demo.actitime.com/login.do")
        driver.implicitly_wait(10)

        username = obj.readData(filepath,sheetname,i,1)
        password = obj.readData(filepath,sheetname,i,2)

        driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
        driver.find_element_by_xpath("//input[@name='pwd']").send_keys(password)
        import time
        time.sleep(6)
        print(driver.title)
        driver.find_element_by_xpath("//div[text()='Login ']").click()
        time.sleep(6)
        print(driver.title)
        if driver.title == "actiTIME - Login":
            print("Test failed")
            obj.writeData(filepath,sheetname, i, 3, "Test failed")
        else:
            print("Test passed")
            obj.writeData(filepath, sheetname, i, 3, "Test passed")
        driver.quit()
        print(i)
login()