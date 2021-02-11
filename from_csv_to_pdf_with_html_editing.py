import pandas as pd
import pdfkit

csv_file = 'final_output.csv'
html_file = csv_file[:-3] + 'html'

df = pd.read_csv('final_output.csv', sep=',')
df.to_html(html_file)

file = open('final_output.html', 'r')
a = file.read()

# file = codecs.open("final_output.html", "r", "utf-8")  # different method to open the html file
# a = file.read()  # Read and save the file in the variable for later use

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

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_file(html_file, 'house_keeping_report.pdf', configuration=config)
