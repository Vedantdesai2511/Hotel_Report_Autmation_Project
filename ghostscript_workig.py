from ctypes.util import find_library
import ctypes
# print(find_library("".join(("gsdll", str(ctypes.sizeof(ctypes.c_voidp) * 8), ".dll"))))

print(find_library(r'C:\Program Files\gs\gs9.53.3\bin\gsdll64.dll'))
print(find_library(r'C:\Program Files (x86)\gs\gs9.53.3\bin\gsdll32.dll'))