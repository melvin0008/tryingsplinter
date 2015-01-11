from splinter import Browser

browser=Browser()
browser.visit('https://mitcoe.herokuapp.com')
browser.fill('username','me@melvinphilips.com')
browser.fill('password','awesome')
button=browser.find_by_value('Log In')
button.click()
if browser.is_text_present('Dashboard'):
	print "Yalla"
else:
	print "Oh no"

browser.quit()

