from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from sys import exit
from datetime import datetime,timedelta,date
import mysql.connector
import random

PATH = "path-for-chrome-driver"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(PATH,options=options)

print('Do you want to continue for today? [Y for Yes/Any key for No]')
ans = input()
print(ans)
if ans == 'Y' or ans == 'y':
    driver.get("https://rocky-plains-03473.herokuapp.com/")
    #click button
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/a[2]/button').click()

    #temperature range random
    temp = round(random.uniform(36.3, 36.6),1)


    driver.find_element_by_xpath('/html/body/div/div/form/div[1]/input').send_keys("201545")
    driver.find_element_by_xpath('/html/body/div/div/form/div[2]/input').send_keys(str(temp))
    driver.find_element_by_xpath('/html/body/div/div/form/div[3]/div[1]/label').click()
    driver.find_element_by_xpath('/html/body/div/div/form/div[5]/div/button').click()
    time.sleep(10)
    driver.save_screenshot("screenshot.png")
    time.sleep(10)
else:
    print("Alright Thanks!")


