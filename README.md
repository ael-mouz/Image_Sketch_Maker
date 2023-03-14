# Image Sketch Maker
This is a simple Python program that converts input images to sketches. It uses the OpenCV library to perform image processing operations such as inversion, Gaussian blur, and division. The resulting sketch is saved as a PNG image file.

## Getting Started
### Prerequisites
To run this program, you will need to have the following software installed on your system:

- Python 3
- openCV library
- libgl1-mesa-glx (for Linux systems only)
You can install the OpenCV library using the following command:

```bash
$ pip install opencv-python
```
On Linux systems, you may also need to install the libgl1-mesa-glx package using the following command:
```bash
$ sudo apt-get install libgl1-mesa-glx
```
### Running the Program
To run the program, navigate to the directory where the program is located and run the following command:
```bash
$ python image_sketch_maker.py
```
The program will prompt you to enter the filename of the input image. Enter the filename and press Enter to generate the sketch. The sketch will be saved as a PNG image file in the same directory as the input image.

To quit the program, enter 'q' when prompted for the filename.
