from selenium import webdriver
import time
import pyautogui
from datetime import datetime
from dateutil.relativedelta import relativedelta
# import tabula
from selenium.webdriver import ActionChains
import hotel_journal_summary_report_analysis
# from selenium.webdriver.support.select import Select
import shutil
import os
import pdftables_api


# driver = webdriver.Chrome("chromedriver.exe")  # open google chrome using chrome driver
#
# action = ActionChains(driver)
#
# link_to_open = "https://www.choiceadvantage.com/choicehotels/sign_in.jsp"


def night_audit_automation():
    driver = webdriver.Chrome("chromedriver.exe")  # open google chrome using chrome driver

    action = ActionChains(driver)

    link_to_open = "https://www.choiceadvantage.com/choicehotels/sign_in.jsp"


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

    time.sleep(5)

    driver.find_element_by_xpath('// *[(@ id = "bannerFavButton_5")]').click()

    time.sleep(5)

    driver.find_element_by_xpath('// *[(@ id = "HotelJournalSummaryReport")]').click()

    time.sleep(5)

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

    # pyautogui.hotkey('enter')

    root_directory = r'C:\Users\vedan\Downloads\{}'

    hotel_journal_summary_report_file_name = (datetime.today() + relativedelta(days=-1)).strftime('%m_%d_%Y') + 'hotel_journal_summary'

    shutil.move(root_directory.format(hotel_journal_summary_report_file_name + '.pdf'), os.path.dirname(os.path.realpath(__file__)))

    c = pdftables_api.Client('ewtqttj2079m')
    c.csv(hotel_journal_summary_report_file_name + '.pdf', root_directory.format(hotel_journal_summary_report_file_name))

    # tabula.convert_into(root_directory.format(hotel_journal_summary_report_file_name + '.pdf'),
    #                     root_directory.format(hotel_journal_summary_report_file_name + '.csv'), output_format="csv",
    #                     stream=True, pages=1)

    time.sleep(5)

    cash_value = hotel_journal_summary_report_analysis.hotel_journal_summary_report_analysis_function(
        root_directory.format(hotel_journal_summary_report_file_name) + '.csv')
    # cash_value = hotel_journal_summary_report_analysis.hotel_journal_summary_report_analysis_function(
    #     'output' + '.csv')

    print(cash_value)

    time.sleep(3)

    # driver.switch_to.window(driver.window_handles[0])

    driver.find_element_by_xpath('//*[(@id = "act8")]').click()

    time.sleep(5)

    # driver.find_element_by_xpath('//*[(@id = "bannerFavButton_14")]').click()

    # time.sleep(5)

    # driver.find_elements_by_class_name("CHI_Button")

    driver.get('https://www.choiceadvantage.com/choicehotels/NightAuditInitialize.init')

    time.sleep(3)

    driver.find_element_by_xpath('// *[(@ id = "runNightAudit")]').click()

    time.sleep(5)

    pyautogui.write(str(cash_value))

    time.sleep(2)

    pyautogui.hotkey('enter')

    time.sleep(10)

    files = [hotel_journal_summary_report_file_name + '.pdf']

    for file in files:
        os.remove(file)
    # driver.find_element_by_xpath('// *[(@ id = "act6")] / option[text() = "Night Audit"]').click()


# night_audit_automation()

# print("I am here")
# time.sleep(1)
#
# driver.get(link_to_open)
#
# driver.execute_script("window.open()")
#
# driver.switch_to.window(driver.window_handles[1])
#
# main_window = driver.switch_to.window(driver.window_handles[0])
#
# print(main_window)
#
# time.sleep(0.5)
#
# e = driver.find_elements_by_class_name("CHI_Cell")
#
# print(e)
# time.sleep(1)
#
# a = driver.find_element_by_xpath("//input")
# e.send_keys("vedantdesai07@gmail.com")

# print(a)
#
# a.send_keys("Vdesai.TXI54")
#
# pyautogui.hotkey('tab')
#
# pyautogui.write('Vbd@251196')
#
# pyautogui.hotkey('tab')
#
# pyautogui.hotkey('enter')
# driver.find_element_by_xpath(
#     '//*[contains(concat( " ", @class, " " ), concat( " ", "CHI_PageSection", " " ))]').click()

# time.sleep(3)

# driver.find_element_by_xpath('//*[(@ id = "act6")]').click()
#
# # driver.find_elements_by_id('menu7_1').click()
#
# # Select.select_by_visible_text('Night Audit')
#
# a = driver.find_elements_by_xpath('//*[text() = "Night Audit"]').click()
#
# print(a)
#
# a = ['<selenium.webdriver.remote.webelement.WebElement (session="b795e3a76eea02332b5b546865cbe69a",
# element="50d68991-fe7d-4b3f-95b8-a3da9c73d10f")>', '<selenium.webdriver.remote.webelement.WebElement (
# session="b795e3a76eea02332b5b546865cbe69a", element="dee98abd-c8d4-4166-8ab6-2d43fcf73e6d")>']
#
# print(a[0])
# # driver.find_elements_by_xpath('//*[text() = "Night Audit"]')[0].click()
# # select by visible text
# # select.select_by_visible_text('Banana')

# driver.get('https://www.choiceadvantage.com/choicehotels/NightAuditInitialize.init')

# root_directory = r'C:\Users\vedan\Downloads\{}'
#
# hotel_journal_summary_report_file_name = (datetime.today() + relativedelta(days=-1)).strftime(
#     '%m_%d_%Y') + 'hotel_journal_summary'

# tabula.convert_into(root_directory.format(hotel_journal_summary_report_file_name + '.pdf'),'abc.csv')

# import camelot
#
# tables = camelot.read_pdf(root_directory.format(hotel_journal_summary_report_file_name + '.pdf', pages="1-end"))
#
# tables.export("camelot_tables.csv", f="csv")

# import pdftables_api

# c = pdftables_api.Client('ewtqttj2079m')
# c.csv(hotel_journal_summary_report_file_name + '.pdf', 'output')

# cash_value = hotel_journal_summary_report_analysis.hotel_journal_summary_report_analysis_function(
#         'output' + '.csv')
#
# print(cash_value)
