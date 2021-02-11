from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from sys import exit
from datetime import datetime,timedelta,date
import mysql.connector
import random

##Global Variables
#mysql config
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="autofill_greatech_covid"
)
#team_json
team = None

def auto_fill():
    PATH = "path-for-chrome-driver"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(PATH,options=options)
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

def get_team_details():
    try: 
        mycursor = mydb.cursor()
        sql = "SELECT * FROM employee_details WHERE activate = 0"
        val = (date,)
        mycursor.execute(sql,val)
        team = mycursor.fetchall()
    except Exception as error:
        print(error)


