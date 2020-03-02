from settings import driver, url1

def test_login():
    driver.get(url1)
    driver.implicitly_wait(6)
    driver.maximize_window()

    pop_up = driver.find_element_by_xpath('//div[@class="Og_iib col col-2-5 _3SWFXF"]').is_displayed()
    if pop_up == True:
        driver.find_element_by_xpath('//input[@class="_2zrpKA _1dBPDZ"]').send_keys(9591593927)
        driver.find_element_by_xpath('//input[@type="password"]').send_keys(9880424831)
        driver.find_element_by_xpath('//button[@class="_2AkmmA _1LctnI _7UHT_c"]').click()

    else:
        driver.find_element_by_xpath('//div[@class="_2aUbKa"]').click()