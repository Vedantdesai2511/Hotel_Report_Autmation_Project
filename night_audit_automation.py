from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.select import Select
import yagmail
import schedule
import os
import tabula
import data_management_house_keeping
import pdfkit
import pandas as pd
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("chromedriver.exe")  # open google chrome using chrome driver

action = ActionChains(driver)

link_to_open = "https://www.choiceadvantage.com/choicehotels/sign_in.jsp"

# open_link(link_to_open)

# from selenium.webdriver.common.action_chains import ActionChains


def night_audit_automation():
    print("I am here")
    time.sleep(1)

    driver.get(link_to_open)

    driver.execute_script("window.open()")

    driver.switch_to.window(driver.window_handles[1])

    main_window = driver.switch_to.window(driver.window_handles[0])

    print(main_window)

    time.sleep(0.5)

    e = driver.find_elements_by_class_name("CHI_Cell")

    print(e)
    time.sleep(1)

    a = driver.find_element_by_xpath("//input")
    # e.send_keys("vedantdesai07@gmail.com")

    print(a)

    a.send_keys("Vdesai.TXI54")

    pyautogui.hotkey('tab')

    pyautogui.write('Vbd@251196')

    pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    # driver.find_element_by_xpath(
    #     '//*[contains(concat( " ", @class, " " ), concat( " ", "CHI_PageSection", " " ))]').click()

    time.sleep(3)

    driver.find_element_by_xpath('// *[(@ id = "bannerFavButton_5")]').click()

    time.sleep(3)

    driver.find_element_by_xpath('// *[(@ id = "HotelJournalSummaryReport")]').click()

    time.sleep(3)

    input_elemwnt = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "hasDatepicker", " " ))]')

    action.triple_click(input_elemwnt).perform()
    # driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "hasDatepicker",
    # " " ))]').click()

    time.sleep(10)


night_audit_automation()
