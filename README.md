# Python-
JP-py-projects
 Pencil Sketch Converter - README
 Overview
The Pencil Sketch Converter application allows users to upload an image, convert it into a pencil sketch, and save the sketch to a designated folder. The application is built using Python, leveraging the OpenCV library for image processing and Tkinter for the graphical user interface (GUI).

Features
1. Upload Image: Users can select an image file from their computer.
2. Convert to Sketch: Converts the uploaded image into a pencil sketch using image processing techniques.
3. Save Sketch: Saves the generated sketch in a folder named `Drawing`, with filenames automatically numbered from `1.png` to `100.png`.
4. Side-by-Side Display: Shows the original image alongside the generated sketch.
   
Requirements
Prerequisites
Before running the application, ensure you have the following:
- Python 3.7 or later
- Required Python packages:
  - `opencv-python`
  - `pillow`

 Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install the required packages using pip:
   ``bash
   pip install opencv-python pillow
   ``

How to Use
1. Save the code into a file, e.g., `pencil_sketch_app.py`.
2. Run the script in your terminal or IDE:
   ```bash
   python pencil_sketch_app.py
   ```
3. Follow these steps in the GUI:
   - Upload Image: Click the "Upload Image" button and select an image file (`.jpg`, `.png`, or `.jpeg`).
   - Convert to Sketch: Click the "Convert to Sketch" button to generate the pencil sketch.
   - Save Sketch: Click the "Save Sketch" button to save the sketch in the `Drawing` folder. The sketches are automatically numbered (`1.png`, `2.png`, etc.).

Explanation of the Code
1.Importing Libraries
- `cv2`: OpenCV library used for image processing tasks like grayscale conversion, inversion, blurring, and creating the pencil sketch.
- `os`: Used to manage file paths and create directories.
- `tkinter`: Python's standard GUI library for creating the user interface.
- `PIL.Image` and `PIL.ImageTk`: Modules from the Pillow library to handle image resizing and display in the Tkinter canvas.

2. Functions
 `upload_image()`
- Allows users to select an image file from their computer.
- Displays the selected image in the "Original Image" canvas.

 `convert_to_sketch()`
- Processes the uploaded image to create a pencil sketch.
- Steps involved:
  1. Convert the image to grayscale using `cv2.cvtColor`.
  2. Invert the grayscale image using `cv2.bitwise_not`.
  3. Apply Gaussian Blur to the inverted image using `cv2.GaussianBlur`.
  4. Invert the blurred image.
  5. Create the sketch by dividing the grayscale image by the inverted blurred image using `cv2.divide`.
- Displays the sketch in the "Pencil Sketch" canvas.

`save_sketch()`
- Saves the generated sketch in a folder named `Drawing`.
- Automatically names the file in ascending order (e.g., `1.png`, `2.png`, ...).
- Creates the `Drawing` folder if it doesn't exist.
- Ensures no more than 100 sketches are saved.

 `display_image()`
- Helper function to resize and display an image on a Tkinter canvas.

3. GUI Components
 Buttons
- Upload Image: Triggers the `upload_image()` function.
- Convert to Sketch: Triggers the `convert_to_sketch()` function.
- Save Sketch: Triggers the `save_sketch()` function.

 Canvases
- Two canvases display:
  - Original image.
  - Generated pencil sketch.

Folder Structure
When you run the application, the following folder will be created automatically:
- `Drawing/`: Contains saved sketch images named as `1.png`, `2.png`, ..., up to `100.png`.

Troubleshooting
1. Error: "Please upload an image first."
   - Ensure you upload an image before clicking "Convert to Sketch."
2. Error: "Maximum limit of 100 images reached!"
   - Clear the `Drawing` folder to make space for new sketches.
3. Tkinter Window Does Not Open
   - Ensure Python and the required libraries are installed correctly.
   - Use a compatible Python version (3.7 or later).
Customization
- Change Image Size: Modify the `resize` parameter in the `display_image()` function to adjust canvas size.
- Change Save Folder Name: Update the `folder_name` variable in the `save_sketch()` function.
Credits
- OpenCV: [https://opencv.org/](https://opencv.org/)
- Pillow (PIL Fork): [https://python-pillow.org/](https://python-pillow.org/)
- Tkinter: Python's standard GUI library.
License
This project is free to use and modify for personal or educational purposes.


