from numpy import around
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')
button = driver.find_element_by_class_name('btn-default')
user_message = driver.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Ow Nice')
button.click()
output_message = driver.find_element_by_id('display')
assert 'Ow Nice' in output_message.text


