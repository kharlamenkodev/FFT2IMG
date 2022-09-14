import os
import sys
import math
from PIL import Image

def convert(path, convertToGgrayScale = False):
    print("Processing file: " + path)

    try:
        file = open(path, 'rb')
    except IOError:
        print("Unable to open file")
        return;

    pixels = bytearray()
    width = 262144;
    height = math.floor(os.stat(file.name).st_size / width)

    if height <= 1:
        sys.exit()

    i = 0
    counter = 0
    progress = 0
    while i < height:
        file.seek(i * width)
        data = file.read(width)

        for byte in data:
            byte = byte * 20

            if byte > 255:
                byte = 255

            if byte < 0:
                byte = 0

            pixels.append(0)
            pixels.append(byte)
            pixels.append(byte)

        i += 1

        if i % math.floor(height/10) == 0:
            counter += 1
            progress += 10
            print(str(progress) + "%")

    image = Image.new("RGB", (width, height))
    image.frombytes(bytes(pixels))

    if convertToGgrayScale:
        image = image.convert("L")

    image.save(os.path.splitext(path)[0] + ".bmp", 'bmp')
    print("Done!")
    file.close()