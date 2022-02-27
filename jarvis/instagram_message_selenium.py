import time
from cv2 import extractChannel
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = "chromedriver"
driver = webdriver.Chrome(path)

driver.get('https://www.instagram.com/')

time.sleep(6)
user_bar = driver.find_element_by_name('username')
user_bar.clear()
user_bar.send_keys("_anas_na_")
pass_bar = driver.find_element_by_name('password')
pass_bar.clear()
pass_bar.send_keys(Instagram_Password)


pass_bar.send_keys(Keys.RETURN)
time.sleep(10)


home = driver.find_element_by_class_name('_8-yf5 ')
home.click()
time.sleep(5)
turn__on = driver.find_element_by_class_name('mt3GC')
turn__on.click()

time.sleep(5)
driver.get('https://www.instagram.com/direct/new/')
time.sleep(2)
search_bar = driver.find_element_by_name('queryBox')
search_bar.send_keys('_rasik_molath_')
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
select_user = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]')
select_user.click()

next_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div/button')
next_button.click()
time.sleep(3)
text_area = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
text_area.send_keys('Hi')
text_area.send_keys(Keys.RETURN)
