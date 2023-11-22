import cv2
import numpy as np
from PIL import Image


# Convert data to binary format
def data2binary(data):
    if type(data) == str:
        return ''.join([format(ord(i), '08b') for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        return [format(i, '08b') for i in data]


# Hide data in the given image
def hide_data(img, data, password):
    data += "$$"  # '$$' --> secret key
    data = password + data
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

    # Iterate pixels from image and update pixel values
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index])
                d_index += 1
            if d_index >= len_data:
                break
    return img


# Encoding
def encode():
    img_name = input("\nEnter image name: ")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    data = input("\nEnter message: ")
    password = input("\nEnter password: ")

    if len(data) == 0:
        raise ValueError("Empty data")

    enc_img = input("\nEnter encoded image name: ")
    enc_data = hide_data(image, data, password)
    cv2.imwrite(enc_img, enc_data)

    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h), Image.ANTIALIAS)

    # Optimize with 65% quality
    if w != h:
        img1.save(enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)


# Decoding
def find_data(img, password):
    bin_data = ""
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

    readable_data = ""
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break
    return readable_data[len(password):-2]


# Decoding with password
def decode():
    img_name = input("\nEnter image name: ")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    password = input("\nEnter password: ")
    msg = find_data(image, password)
    print("\nYour message: " + msg)


# Main steganography function
def steganography():
    x = 1
    while x != 0:
        print('''\nImage steganography
        1. Encode
        2. Decode''')
        u_in = int(input("\nEnter your choice: "))

        if u_in == 1:
            encode()
        else:
            decode()

        x = int(input("\nEnter 1 to continue, otherwise 0: "))


steganography()
