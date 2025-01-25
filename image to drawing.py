import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Button, Canvas, PhotoImage
from PIL import Image, ImageTk
import numpy as np
import time

# Function to upload an image
def upload_image():
    global original_image, file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if file_path:
        original_image = cv2.imread(file_path)
        display_image(file_path, canvas_original)
        label_message.config(text="Image uploaded successfully!", fg="green")

# Function to apply pencil sketch effect with animation
def convert_to_sketch():
    if not file_path:
        label_message.config(text="Please upload an image first.", fg="red")
        return

    global sketch_image
    # Convert the original image to gray scale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    # Invert the blurred image
    inverted_blur = cv2.bitwise_not(blurred_image)
    # Create the pencil sketch
    sketch_image = cv2.divide(gray_image, inverted_blur, scale=256.0)

    # Save the sketch image temporarily
    temp_path = "temp_sketch.png"
    cv2.imwrite(temp_path, sketch_image)

    # Animate the drawing effect
    animate_drawing(temp_path, canvas_sketch)

    label_message.config(text="Pencil sketch created successfully!", fg="green")

# Function to animate the drawing process
def animate_drawing(image_path, canvas):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    img_copy = np.zeros_like(img)  # Start with a blank image

    for i in range(0, 101, 5):  # Gradually reveal the sketch in steps
        alpha = i / 100.0
        img_copy = cv2.addWeighted(img, alpha, img_copy, 1 - alpha, 0)
        temp_animation_path = "temp_animation.png"
        cv2.imwrite(temp_animation_path, img_copy)
        display_image(temp_animation_path, canvas)
        canvas.update()  # Update the canvas to reflect changes
        time.sleep(0.05)  # Pause briefly to create animation effect

# Function to save the sketch image
def save_sketch():
    if sketch_image is None:
        label_message.config(text="Please create a sketch first.", fg="red")
        return

    # Create the Drawing folder if it doesn't exist
    folder_name = "Drawing"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Find the next available filename in the folder
    existing_files = sorted([int(f.split('.')[0]) for f in os.listdir(folder_name) if f.isdigit()])
    next_index = existing_files[-1] + 1 if existing_files else 1

    if next_index > 100:
        label_message.config(text="Maximum limit of 100 images reached!", fg="red")
        return

    # Save the sketch with the next available name
    save_path = os.path.join(folder_name, f"{next_index}.png")
    cv2.imwrite(save_path, sketch_image)
    label_message.config(text=f"Sketch saved as {save_path}", fg="green")

# Helper function to display an image on a canvas
def display_image(image_path, canvas):
    img = Image.open(image_path)
    img_resized = img.resize((300, 300))  # Resize to fit the canvas
    img_tk = ImageTk.PhotoImage(img_resized)
    canvas.img_tk = img_tk  # Keep a reference to avoid garbage collection
    canvas.create_image(0, 0, anchor="nw", image=img_tk)

# Initialize the GUI window
root = tk.Tk()
root.title("Pencil Sketch Converter")
root.geometry("800x500")
root.configure(bg="#e0f7fa")

# Global variables
file_path = None
original_image = None
sketch_image = None

# Labels and Buttons
label_title = Label(root, text="Pencil Sketch Converter", font=("Helvetica", 20, "bold"), bg="#00796b", fg="white", padx=10, pady=10)
label_title.pack(fill="x")

label_message = Label(root, text="", font=("Arial", 12), bg="#e0f7fa")
label_message.pack()

frame_buttons = tk.Frame(root, bg="#e0f7fa")
frame_buttons.pack(pady=10)

button_upload = Button(frame_buttons, text="Upload Image", command=upload_image, bg="#004d40", fg="white", font=("Arial", 12), padx=10, pady=5)
button_upload.grid(row=0, column=0, padx=10)

button_convert = Button(frame_buttons, text="Convert to Sketch", command=convert_to_sketch, bg="#0288d1", fg="white", font=("Arial", 12), padx=10, pady=5)
button_convert.grid(row=0, column=1, padx=10)

button_save = Button(frame_buttons, text="Save Sketch", command=save_sketch, bg="#d84315", fg="white", font=("Arial", 12), padx=10, pady=5)
button_save.grid(row=0, column=2, padx=10)

# Canvases for original and sketch images
frame_images = tk.Frame(root, bg="#e0f7fa")
frame_images.pack(pady=10)

canvas_original = Canvas(frame_images, width=300, height=300, bg="#c8e6c9")
canvas_original.grid(row=0, column=0, padx=10)
Label(frame_images, text="Original Image", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=0)

canvas_sketch = Canvas(frame_images, width=300, height=300, bg="#ffcdd2")
canvas_sketch.grid(row=0, column=1, padx=10)
Label(frame_images, text="Pencil Sketch", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=1)

# Run the application
root.mainloop()
