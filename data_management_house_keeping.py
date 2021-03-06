import tabula
import pandas as pd
from datetime import datetime
import pdfkit
import time


def house_keeping_report_function(report_1, report_2, room_list=None):
    if room_list is None:
        room_list = [107, 211, 202]

    df1 = pd.read_csv(report_1)
    print("ebgubesibwgiowebiuogbwiuoebgiuwbeiugobwoiegwerhwthrtwjwr")
    print(df1)
    print('euwtgywehuitghiuwethwtjrywjrywjyrhrywjhyrejyrj')

    df2 = pd.read_csv(report_2)

    print(df2)

    print('raguy8uarehhehtwjryejyetjryjretjreyjrej')

    print(df1)
    print(df2)
    print("#########################")
    a = df2.drop(df2.loc[df2['Stay/C/O'] == "Stay"].index)
    print(a)

    for i in room_list:
        df1.drop(df1.loc[df1['Room'] == i].index, inplace=True)

    print("#################################")
    print(df1)
    final_output = a.append(df1)

    print(final_output)

    final_output.drop(['People', 'Status', 'Service', 'Housekeeper', 'Update', 'Notes', 'Arrival', 'Departure', 'Last Clean'], axis=1, inplace=True)
    final_output.reset_index(drop=True, inplace=True)

    print(final_output)
    # final_output.to_csv("final_output.csv")

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    csv_file = 'final_output.csv'
    html_file = csv_file[:-3] + 'html'

    # df = pd.read_csv('final_output.csv', sep=',')
    final_output.to_html(html_file)

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

    pdfkit.from_file(html_file, 'house_keeping_report.pdf', configuration=config)

    time.sleep(2)


if __name__ == "__main__":
    root_directory = r'C:\Users\vedan\Downloads\{}'

    tabula.convert_into(root_directory.format('abc' + '.pdf'),
                        root_directory.format('abc' + '.csv'), output_format="csv", stream=True,
                        pages=1)

    house_keeping_report_function(root_directory.format('abc' + '.csv'), root_directory.format('abcd' + '.csv'))


# root_directory = r'C:\Users\vedan\Downloads\{}'
#
# name_of_the_file_HK_1_ = (datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_1'
# name_of_the_file_HK_2_ = (datetime.today()).strftime('%m_%d_%Y') + 'house_keeping_list_2'
#
# # tabula.convert_into(root_directory.format(name_of_the_file_HK_1_ + '.pdf'), root_directory.format(name_of_the_file_HK_1_ + '.csv'), output_format="csv", stream=True, pages=1)
# # tabula.convert_into(root_directory.format(name_of_the_file_HK_2_ + '.pdf'), root_directory.format(name_of_the_file_HK_2_ + '.csv'), output_format="csv", stream=True, pages=1)
#
# house_keeping_report_function(root_directory.format(name_of_the_file_HK_1_ + '.csv'), root_directory.format(name_of_the_file_HK_2_ + '.csv'), room_list=None)
#
# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#
# csv_file = 'final_output.csv'
# html_file = csv_file[:-3]+'html'
#
# df = pd.read_csv('final_output.csv', sep=',')
# df.to_html(html_file)
#
# # with open('header.html', 'r') as f:
# #     html_string = f.read()
#
# options = {
#     'page-size': 'Letter',
#     'margin-top': '0.75in',
#     'margin-right': '0.75in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.75in',
#     'encoding': "UTF-8",
#     'no-outline': None,
#     'header-html': "C:/Users/vedan/PycharmProjects/upfib_algo_trading/header.html"
# }
#
# pdfkit.from_file(html_file, 'house_keeping_report.pdf', configuration=config, options=options)
# pdfkit.from_file(html_file, 'house_keeping_report.pdf', configuration=config)
