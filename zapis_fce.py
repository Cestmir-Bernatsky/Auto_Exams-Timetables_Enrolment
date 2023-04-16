import time
import datetime
import selenium
from tkinter import *
from selenium import webdriver

def sign_timetable(name, password):

    PATH = "chromedriver.exe"

    driver = webdriver.Chrome(PATH)
    driver.get('https://www.stag.upol.cz/portal/')

    stag_web = driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[3]/td/input')
    stag_web.click()

    login_box = driver.find_element_by_xpath('//*[@id="username"]')
    login_box.send_keys(name)

    pass_box = driver.find_element_by_xpath('//*[@id="password"]')
    pass_box.send_keys(password)

    #prihlaseni

    log_button = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div/div[3]/div/button')
    log_button.click()

    moje_stud = driver.find_element_by_xpath('/html/body/div[1]/div[4]/ul/li[2]/a')
    moje_stud.click()

    predzapis = driver.find_element_by_xpath('//*[@id="app_page_menu"]/ul/li[10]/a')
    predzapis.click()

    vyber = driver.find_element_by_xpath('//*[@id="KrouzekPredzapisPortletFormKrouzkySelect"]')
    vyber.click()
    vyber.send_keys('5ZUB1A')
    vyber.click()

    now = datetime.datetime.today()
    print(now)
    future = datetime.datetime(now.year, now.month, 14, 10, 0,0)
    print(future)
    print(future-now)

    time.sleep((future-now).seconds)
    driver.refresh()

    vyber2 = driver.find_element_by_xpath('//*[@id="KrouzekPredzapisPortletFormKrouzkySelect"]')
    vyber2.click()
    vyber2.send_keys('5ZUB1A')
    vyber2.click()

    zapsat = driver.find_element_by_xpath('//*[@id="cpa_6468"]/div[3]/div[3]/table/tbody/tr/td[3]/input')
    zapsat.click()
