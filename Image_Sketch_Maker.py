import cv2
import os
# pip install opencv-python
# sudo apt-get install libgl1-mesa-glx
# export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu

# Create a new folder to store the sketches
if not os.path.exists("sketches"):
    os.mkdir("sketches")
while True:
	# Ask the user for the filename of the input image
	input_filename = input("Enter the input image (or 'q' to quit): ")
	# Check if the user wants to quit
	if input_filename == "q":
		break
	# Load the input image
	image = cv2.imread(input_filename)
	# Convert the image to grayscale
	grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# Invert the grayscale image
	invert = cv2.bitwise_not(grey_img)
	# Apply Gaussian blur to the inverted image
	blur = cv2.GaussianBlur(invert, (21, 21), 0)
	# Invert the blurred image
	invertedblur = cv2.bitwise_not(blur)
	# Divide the grayscale image by the inverted blurred image
	sketch = cv2.divide(grey_img, invertedblur, scale=256)
	# Generate a filename for the output sketch
	output_filename = os.path.join("sketches", os.path.basename(input_filename).split(".")[0] + "_sketch.png")
	# Save the sketch to a file
	cv2.imwrite(output_filename, sketch)
	# Print a message to confirm that the sketch was saved
	print(f"Sketch saved to '{output_filename}'\n")
