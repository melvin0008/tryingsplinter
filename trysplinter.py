from splinter import Browser
import time

browser=Browser()
browser.visit('https://www.juliabox.org/hostlaunchipnb/')
browser.fill('Email','testjuliamechanize')
browser.fill('Passwd','testjulia')
button=browser.find_by_value('Sign in')
button.click()
time.sleep(30)
if browser.is_text_present('IJulia'):
	print "Wow"
else:
	print "Oh no"

browser.quit()

