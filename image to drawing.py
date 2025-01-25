import tkinter as tk
from tkinter import filedialog
from tkinter import Label
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageEnhance

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = Image.open(file_path)
        display_image(original_image, original_image_label)

        # Convert the image to grayscale
        gray_image = ImageOps.grayscale(original_image)
        
        # Invert the grayscale image
        inverted_image = ImageOps.invert(gray_image)
        
        # Blur the inverted image
        blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(15))
        
        # Blend the grayscale image with the blurred inverted image
        blend = Image.blend(gray_image, blurred_image, 0.2)
        
        # Enhance the edges to simulate pencil strokes
        edge_enhanced_image = blend.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
        # Increase contrast to make the drawing effect more pronounced
        final_sketch = ImageEnhance.Contrast(edge_enhanced_image).enhance(2.0)
        
        display_image(final_sketch, sketch_image_label)

def display_image(image, label):
    # Resize the image to fit within the label
    image.thumbnail((400, 400))
    img_display = ImageTk.PhotoImage(image)
    label.config(image=img_display)
    label.image = img_display  # Keep a reference to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("Image to Drawing Converter")

# Create labels to display the original and sketch images
original_image_label = Label(root)
original_image_label.pack(side="left", padx=10, pady=10)

sketch_image_label = Label(root)
sketch_image_label.pack(side="right", padx=10, pady=10)

# Create a button to upload an image
upload_button = tk.Button(root, text="Upload Image", command=open_image)
upload_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
