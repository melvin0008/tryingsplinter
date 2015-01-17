import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def testjulia():
    """Docstring for testselenium.testjulia
        ========================================
        testjulia()

    """
    driver = webdriver.Firefox()
    driver.get("https://www.juliabox.org/hostlaunchipnb/")

    emailid = driver.find_element_by_id("Email")
    emailid.send_keys("youremailID")


    passw = driver.find_element_by_id("Passwd")
    passw.send_keys("yourpassword")


    signin = driver.find_element_by_id("signIn")
    signin.click()

    time.sleep(20)
    ijulia = driver.find_element_by_id('ijulia-frame')
    driver.switch_to_frame(ijulia)
    newnotebook = driver.find_element_by_id("new_notebook")
    newnotebook.click()

testjulia()
