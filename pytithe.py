

#!/usr/bin/python
import sys
#print(str(sys.argv))
try: 
    username = str(sys.argv[1])
    password = str(sys.argv[2])
    tithe_amt = str(sys.argv[3])

    #pip install selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from time import sleep
    #headless mode
    options = Options()
    options.headless = True
    try:
        options.headless = sys.argv[4]
    except:
        pass
    DRIVER_PATH = 'chromedriver'

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("https://id.churchofjesuschrist.org/signin")
    print('-----------Title------------: ',driver.title)
    time.sleep(3)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_id('okta-signin-submit').click()
    time.sleep(2)
    driver.find_elements_by_tag_name("input")[0].send_keys(password)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(4)
    driver.get("https://donations.churchofjesuschrist.org/donations/#/donation/step1")
    time.sleep(8)
    driver.find_element_by_xpath("//*[@class='whiteSlip']//input[@ng-model='slipLine.amount']").send_keys(tithe_amt)
    driver.find_element_by_xpath("//*[@class='whiteSlip']//div[@class='btnContainer']//a").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@class='whiteSlip steps bank']//a[@class='btn btn-primary floatR']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@class='whiteSlip steps']//a[@class='btn btn-primary floatR']").click()
    time.sleep(10)
    driver.quit()
    print(tithe_amt, 'dollars were successfully tithed!')
except:
    print('Some type of error occurred!')