# Image-stegnography
This Python code implements a simple image steganography project using the Least Significant Bit (LSB) method. Here's a brief explanation:

Data to Binary Conversion:

The data2binary function converts input data (either a string, bytes, or numpy array) into its binary representation.
Hide Data in Image:

The hide_data function takes an image and data as input and hides the data in the image using the LSB method. It also includes a password in the hidden data.
Encoding:

The encode function prompts the user to input an image file, a message, and a password. It then encodes the message into the image using the hide_data function and saves the result as a new image file.
Find Data in Image:

The find_data function extracts hidden data from an image using the LSB method. It also takes a password as input and uses it during decoding.
Decoding:

The decode function prompts the user to input an encoded image file and a password. It then decodes the hidden message using the find_data function and prints the result.
Main Steganography Function:

The steganography function is the main control loop. It allows the user to choose between encoding and decoding operations and continues until the user decides to exit.
In summary, this code allows users to hide messages in images using steganography and retrieve them later with the correct password. The encoding process embeds the message in the image, and the decoding process extracts the hidden message using the provided password.

## Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 'opencv,pillow and numpy'
```bash
pip install opencv-python
pip install pillow
pip install numpy
```
## usage

step-1. clonning--> git clone repo. or download zip file  

step-2. run 'python imgstegno.py'

step-3. give respective inputes and get outputs

