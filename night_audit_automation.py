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

    input_elemwnt = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", '
                                                 '"hasDatepicker", " " ))]')

    action.triple_click(input_elemwnt).perform()  # wrote triple click function my self in the selenium source code
    # that's so cool
    # driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "hasDatepicker",
    # " " ))]').click()

    time.sleep(2)

    pyautogui.hotkey('backspace')

    time.sleep(0.5)

    pyautogui.write((datetime.today() + relativedelta(days=-1)).strftime('%m/%d/%Y'))

    time.sleep(0.5)

    driver.find_element_by_xpath('// *[(@ id = "doSubmit")]').click()

    time.sleep(5)

    pyautogui.keyDown('ctrl')
    pyautogui.press('s')
    pyautogui.keyUp('ctrl')

    time.sleep(2)
    # (datetime.today()).strftime('%m_%d_%Y')
    # name_of_the_file_HK_1 = (datetime.today() + relativedelta(days=-1)).strftime('%m_%d_%Y') + 'hotel_journal_summary'
    pyautogui.write((datetime.today() + relativedelta(days=-1)).strftime('%m_%d_%Y') + 'hotel_journal_summary')

    time.sleep(1)

    pyautogui.hotkey('enter')

    time.sleep(1)

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(1)

    pyautogui.hotkey('enter')

    root_directory = r'C:\Users\vedan\Downloads\{}'

    hotel_journal_summary_report_file_name = (datetime.today() + relativedelta(days=-1)).strftime('%m_%d_%Y') + 'hotel_journal_summary '

    tabula.convert_into(root_directory.format(hotel_journal_summary_report_file_name + '.pdf'),
                        root_directory.format(hotel_journal_summary_report_file_name + '.csv'), output_format="csv",
                        stream=True, pages=1)


night_audit_automation()
