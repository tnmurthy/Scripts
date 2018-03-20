#  How to start using ChromeDriver for testing your website on desktop
# steps to setup your tests for running with ChromeDriver:
# Ensure Chromium/Google Chrome is installed in a recognized location
# Download the ChromeDriver binary for your platform
# Help WebDriver find the downloaded ChromeDriver executable

import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/saanvi/Downloads/Softwares/chromedriver_win32/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()


# ChromeDriver class starts the ChromeDriver server process at creation and terminates it when quit is called.
# This can waste a significant amount of time for large test suites where a ChromeDriver instance is created per test.
#
# import time
#
# from selenium import webdriver
# import selenium.webdriver.chrome.service as service
#
# service = service.Service('C:/Users/saanvi/Downloads/Softwares/chromedriver_win32/chromedriver')
# service.start()
# capabilities = {'chrome.binary': 'C:/Users/saanvi/Downloads/Softwares/chromedriver_win32/chromedriver'}
# driver = webdriver.Remote(service.service_url, capabilities)
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# driver.quit()