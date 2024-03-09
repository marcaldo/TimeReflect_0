import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class ImageLocalLoader:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
    
    def load_image(self, image_path):
        try:
            # Open the image from the response content
            image = Image.open(image_path)
            # Resize the image to fit the screen size
            width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            image = image.resize((width, height))
            # Convert the image to a format that Tkinter can display
            photo = ImageTk.PhotoImage(image)
            # Display the image on the canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            # Keep a reference to the photo to prevent garbage collection
            self.canvas.image = photo

        except Exception as e:
            # Display an error message if an exception occurs
            # self.error_label = tk.Label(self, fg="red", text="")
            #self.error_label.pack()
            self.error_label.config(text=f"An error occurred: {str(e)}")
            self.error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the error label over the canvas
