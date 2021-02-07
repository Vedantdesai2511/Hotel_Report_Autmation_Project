import pdfkit
import pandas as pd

import pdfkit
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# path_wkhtmltopdf = r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)


# pd.read_csv('final_output.csv')
csv_file = 'final_output.csv'
html_file = csv_file[:-3]+'html'
# pdf_file = csv_file[:-3]+'pdf'

df = pd.read_csv('final_output.csv', sep=',')
df.to_html(html_file)
pdfkit.from_file(html_file, 'house_keeping_report.pdf', configuration=config)

# pdfkit.from_file('final_output.csv',
#                  'house_keeping_report.pdf', configuration=config)



# config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')
# pdfkit.from_file('final_output.csv',
#                  'house_keeping_report.pdf',
#                  configuration=config
# )
