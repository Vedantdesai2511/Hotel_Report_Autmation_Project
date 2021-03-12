import tabula
import pandas as pd
from datetime import datetime
import pdfkit
from print_on_the_specific_printer import print_the_file
import re


def house_keeping_report_function(report_1, report_2, room_list=None):
    df1 = pd.read_csv(report_1)
    # df2 = pd.read_csv(report_2)

    print(df1.columns)
    # print(df2)
    df1.drop([0, 1], inplace=True)
    df1.drop(df1.tail(1).index, inplace=True)

    print(df1['Housekeeping Check-Off List'])
    a = str(df1['Housekeeping Check-Off List'])
    # print(str(a)[0])

    data = {}

    print(df1)

    for i in ['Room', 'Status', 'Condition']:
        data[i] = []

    for idx, i in enumerate(df1['Housekeeping Check-Off List']):
        print(idx)
        # a = str(df1['Housekeeping Check-Off List'])
        temp = re.findall(r'\d+', i)
        res = list(map(int, temp))
        data['Room'].append(res[-1])
        data['Status'].append('VAC')
        data['Condition'].append('Dirty')

    print(data)

    df1 = pd.read_csv(report_2)

    df1.drop([0, 1], inplace=True)
    df1.drop(df1.tail(1).index, inplace=True)

    a = df1.drop(df1.loc[df1['Unnamed: 5'] == "Stay"].index)
    print(a)

    for idx, i in enumerate(a['Housekeeping Check-Off List']):
        print(idx)
        # a = str(df1['Housekeeping Check-Off List'])
        temp = re.findall(r'\d+', i)
        res = list(map(int, temp))
        data['Room'].append(res[-1])
        data['Status'].append('C/O')
        data['Condition'].append('Dirty')

    print(data)
    df = pd.DataFrame(data, columns=['Room', 'Status', 'Condition'])
    # print(df)
    # df.reset_index(drop=True, inplace=True)
    # print(df)
    # df.to_csv("final_output_.csv")

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # csv_file = 'final_output_.csv'
    html_file = 'final_output_.html'

    # df = pd.read_csv('final_output_.csv', sep=',')
    # print(df)
    df.to_html(html_file)

    file = open('final_output_.html', 'r')
    a = file.read()

    # file = codecs.open("final_output.html", "r", "utf-8")  # different method to open the html file
    # a = file.read()

    f = open('final_output_.html', 'w')

    message = """<style>
        th {
          font-size: 30px;
        }
    
        td {
          font-size: 45px;
        }
        </style>
    
        """ + a

    # print(f.read())

    f.write(message)
    f.close()

    print("Printing combined House-keeping Report")

    pdfkit.from_file(html_file, 'house_keeping_report_.pdf', configuration=config)

    # print_the_file('house_keeping_report_.pdf')


root_directory = r'C:\Users\vedan\Downloads\{}'

house_keeping_report_function(root_directory.format('abc.csv'), root_directory.format('abcd.csv'))
