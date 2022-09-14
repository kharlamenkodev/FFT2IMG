# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

import os
import sys
from converter import convert

if __name__ == '__main__':

    dirPath = "E://"
    convertToGrayScale = True

    if not (os.path.exists(dirPath)):
        print("Folder not exist!")

    for dirs, folder, files in os.walk(dirPath):
        for file in files:
            if file.endswith(".fft") | file.endswith(".FFT"):
                path = dirPath + os.path.basename(file)
                convert(path,convertToGrayScale)
        break






