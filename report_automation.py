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
from night_audit_automation import night_audit_automation
from print_on_the_specific_printer import print_the_file
import pdftables_api


def report_automation():
    link_to_open = "https://www.choiceadvantage.com/choicehotels/sign_in.jsp"

    # root_directory = r'C:\Users\vedan\Downloads\{}'
    # open_link(link_to_open)

    from selenium.webdriver.common.action_chains import ActionChains

    def report_download_automation():
        print("I am here")
        time.sleep(1)

        driver.get(link_to_open)

        driver.execute_script("window.open()")

        driver.switch_to.window(driver.window_handles[1])

        main_window = driver.switch_to.window(driver.window_handles[0])

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

        driver.find_element_by_xpath('// *[(@ id = "OccupancySnapshotReport")]').click()

        time.sleep(5)

        a = driver.find_element_by_class_name('datepickerField')

        print(a)

        driver.find_element_by_class_name('datepickerField').click()

        time.sleep(3)

        pyautogui.hotkey('tab')

        time.sleep(1)

        pyautogui.hotkey('backspace')

        time.sleep(1)

        # for i in range(3):
        #     pyautogui.hotkey('')
        #
        # pyautogui.hotkey('backspace')
        #
        pyautogui.write((datetime.today() + relativedelta(months=+3)).strftime('%m/%d/%Y'))

        for i in range(3):
            time.sleep(0.2)
            pyautogui.hotkey('tab')

        pyautogui.hotkey('enter')
        # N = 1  # number of times you want to press TAB

        time.sleep(10)

        pyautogui.keyDown('ctrl')
        pyautogui.press('s')
        pyautogui.keyUp('ctrl')

        time.sleep(5)
        # (datetime.today()).strftime('%m_%d_%Y')
        name_of_the_file = (datetime.today()).strftime('%m_%d_%Y') + 'report'
        pyautogui.write((datetime.today()).strftime('%m_%d_%Y') + 'report')

        time.sleep(5)

        pyautogui.hotkey('enter')

        time.sleep(5)

        driver.switch_to.window(driver.window_handles[0])

        driver.find_element_by_xpath('// *[(@ id = "goBack")]').click()

        time.sleep(5)

        driver.find_element_by_xpath('// *[(@ id = "HousekeepingCheckOffListReport")]').click()

        time.sleep(5)

        driver.find_element_by_xpath('// *[(@ id = "doSubmit")]').click()

        time.sleep(5)

        pyautogui.keyDown('ctrl')
        pyautogui.press('s')
        pyautogui.keyUp('ctrl')

        time.sleep(2)
        # (datetime.today()).strftime('%m_%d_%Y')
        name_of_the_file_HK_1 = (datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_1'
        pyautogui.write((datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_1')

        time.sleep(1)

        pyautogui.hotkey('enter')

        time.sleep(5)

        pyautogui.keyDown('ctrl')
        pyautogui.press('p')
        pyautogui.keyUp('ctrl')

        time.sleep(5)

        pyautogui.hotkey('enter')

        time.sleep(5)

        driver.switch_to.window(driver.window_handles[0])

        time.sleep(3)

        # select by visible text
        Select(driver.find_element_by_xpath('// select')).select_by_visible_text('Occupied')

        driver.find_element_by_xpath('// *[(@ id = "doSubmit")]').click()

        time.sleep(5)

        time.sleep(5)

        pyautogui.keyDown('ctrl')
        pyautogui.press('p')
        pyautogui.keyUp('ctrl')

        time.sleep(5)

        pyautogui.hotkey('enter')

        time.sleep(5)

        pyautogui.keyDown('ctrl')
        pyautogui.press('s')
        pyautogui.keyUp('ctrl')

        time.sleep(2)
        # (datetime.today()).strftime('%m_%d_%Y')
        name_of_the_file_HK_2 = (datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_2'
        pyautogui.write((datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_2')

        time.sleep(1)

        pyautogui.hotkey('enter')

        time.sleep(1)

        driver.close()

        return name_of_the_file, name_of_the_file_HK_1, name_of_the_file_HK_2
        # driver.close()
        # actions = ActionChains(driver)
        # for _ in range(N):
        #     time.sleep(0.5)
        #     actions = actions.send_keys(Keys.TAB)
        # actions.perform()
        #
        # actions.send_keys("abc")
        #
        # actions.perform()
        # a = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "CHI_PageSection", " " ))]')
        #
        # time.sleep(1)
        # a.sendKeys(Keys.TAB)
        # time.sleep(0.5)
        # a.sendKeys(Keys.TAB)
        # a.sendKeys(Keys.TAB)
        # a = driver.find_element_by_xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "CHI_Row", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "CHI_Row", " " ))]//input')

        # a[1].send_keys("agsfdyuigasif")

    driver = webdriver.Chrome("chromedriver.exe")  # open google chrome using chrome driver

    (name_of_the_file_, name_of_the_file_HK_1_, name_of_the_file_HK_2_) = report_download_automation()

    root_directory = r'C:\Users\vedan\Downloads\{}'

    yagmail.register("reportautomation1@gmail.com", "Report@automation123")  # put sender mail id and password here

    def email_occupancy_snap_shot_reports_using_libraries(receiver):
        # receiver = ["reportautomation1@gmail.com"]
        # receiver = ["sumit@dalwadi.com", "nathan.overton@dalwadi.com"]
        body = "Report"
        # root_directory = r'C:\Users\vedan\Downloads\{}.pdf'
        filenames = root_directory.format(name_of_the_file_ + '.pdf')

        yag = yagmail.SMTP("reportautomation1@gmail.com")
        yag.send(
            to=receiver,
            subject="Report_" + (datetime.today()).strftime('%m_%d_%Y'),
            contents=body,
            attachments=filenames,
        )

        print("Report sent")

    email_occupancy_snap_shot_reports_using_libraries(["sumit@dalwadi.com", "nathan.overton@dalwadi.com"])
    email_occupancy_snap_shot_reports_using_libraries(["reportautomation1@gmail.com"])

    name_of_the_file_HK_1_ = (datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_1'
    name_of_the_file_HK_2_ = (datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_2'

    tabula.convert_into(root_directory.format(name_of_the_file_HK_1_ + '.pdf'),
                        root_directory.format(name_of_the_file_HK_1_ + '.csv'), output_format="csv", stream=True,
                        pages=1)
    tabula.convert_into(root_directory.format(name_of_the_file_HK_2_ + '.pdf'),
                        root_directory.format(name_of_the_file_HK_2_ + '.csv'), output_format="csv", stream=True,
                        pages=1)

    data_management_house_keeping.house_keeping_report_function(root_directory.format(name_of_the_file_HK_1_ + '.csv'),
                                                               root_directory.format(name_of_the_file_HK_2_ + '.csv'),
                                                               room_list=None)

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    csv_file = 'final_output.csv'
    html_file = csv_file[:-3] + 'html'

    df = pd.read_csv('final_output.csv', sep=',')
    df.to_html(html_file)

    file = open('final_output.html', 'r')
    a = file.read()

    # file = codecs.open("final_output.html", "r", "utf-8")  # different method to open the html file
    # a = file.read()

    f = open('final_output.html', 'w')

    message = """<style>
        th {
          font-size: 20px;
        }

        td {
          font-size: 30px;
        }
        </style>

        """ + a

    # print(f.read())

    f.write(message)
    f.close()

    print("Printing combined House-keeping Report")

    pdfkit.from_file(html_file, 'house_keeping_report.pdf', configuration=config)

    time.sleep(2)

    def email_house_keeping_check_off_list_reports_using_libraries():
        receiver = ["econolodgehtx@dalwadi.com"]
        # receiver = ["reportautomation1@gmail.com"]
        body = ""
        # root_directory = r'C:\Users\vedan\Downloads\{}.pdf'
        filenames = ['house_keeping_report.pdf', root_directory.format(name_of_the_file_HK_1_ + '.pdf'), root_directory.format(name_of_the_file_HK_2_ + '.pdf')]

        yag = yagmail.SMTP("reportautomation1@gmail.com")
        yag.send(
            to=receiver,
            subject="HK_Report_" + (datetime.today()).strftime('%m_%d_%Y'),
            contents=body,
            attachments=filenames,
        )

        print("House keeping combined report sent")

    # email_house_keeping_check_off_list_reports_using_libraries()

    # print_the_file('house_keeping_report.pdf')

    time.sleep(10)

    root_directory = r'C:\Users\vedan\Downloads\{}'
    files = [root_directory.format(name_of_the_file_ + '.pdf'), root_directory.format(name_of_the_file_HK_1_ + '.pdf'),
             root_directory.format(name_of_the_file_HK_2_ + '.pdf'),root_directory.format(name_of_the_file_HK_2_ + '.csv'), root_directory.format(name_of_the_file_HK_1_ + '.csv')]

    for file in files:
        os.remove(file)


schedule.every().day.at("07:30").do(report_automation)
# schedule.every().day.at("01:05").do(night_audit_automation)03_08_2021report
# night_audit_automation()
# report_automation()

while True:
    schedule.run_pending()
    time.sleep(5)
