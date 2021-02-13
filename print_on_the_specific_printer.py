# import win32printing
#
# GHOSTSCRIPT_PATH = "C:\\path\\to\\GHOSTSCRIPT\\bin\\gswin32.exe"
# GSPRINT_PATH = "C:\\path\\to\\GSPRINT\\gsprint.exe"
#
# # YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
# currentprinter = win32printing.GetDefaultPrinter()
#
# win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "PDFFile.pdf"', '.', 0)

import os
import psutil
import time


def print_the_file(file_name):
    os.startfile(file_name, "print")
    time.sleep(5)
    for p in psutil.process_iter():  # Close Acrobat after printing the PDF
        if 'AcroRd' in str(p):
            p.kill()


# import cups
#
# conn = cups.Connection()
# printers = conn.getPrinters()
# printer_name = printers.keys()[0]
# conn.printFile(printer_name,'/home/pi/Desktop/a.pdf',"",{})
