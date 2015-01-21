import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def facebookpost():
    """Docstring for testselenium.facebookpost
        ========================================
        testjulia()
    """
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com")

    emailid = driver.find_element_by_id("email")
    emailid.send_keys("youremailid")


    passw = driver.find_element_by_id("pass")
    passw.send_keys("yourpassword")


    signin = driver.find_element_by_id("u_0_n")
    signin.click()

    query=driver.find_element_by_id('u_0_10')
    query.send_keys("your post")

    newnotebook = driver.find_element_by_xpath('//button[text()="Post"]')
    newnotebook.click()

facebookpost()
