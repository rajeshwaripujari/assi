from selenium import webdriver
chromepath=r"C:\Users\Basavarajeshwri\PycharmProjects\ptest\pytest_pack\driver\chromedriver.exe"
driver=webdriver.Chrome(chromepath)
url1 = "http://www.flipkart.com"
urls={"url1":"http://www.gmail.com",
      "url2":"http://www.flipkart.com",
      "url3":"http://www.amazon.com",
      "url4":"http://www.facebook.com",
      "url5":"https://demo.actitime.com/login.do"}
url = ["http://www.gmail.com","http://www.flipkart.com","http://www.amazon.com","http://www.facebook.com"]