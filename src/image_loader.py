import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class ImageLoader:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        # self.error_label = tk.Label(root, fg="red", text="")
        # self.error_label.pack()
    
    def load_image(self, image_url):
        try:
            # Make a GET request to the image URL
            response = requests.get(image_url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Open the image from the response content
                image = Image.open(BytesIO(response.content))
                # Resize the image to fit the screen size
                width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
                image = image.resize((width, height))
                # Convert the image to a format that Tkinter can display
                photo = ImageTk.PhotoImage(image)
                # Display the image on the canvas
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                # Keep a reference to the photo to prevent garbage collection
                self.canvas.image = photo
            else:
                # Display an error message if the request was unsuccessful
                self.error_label.config(text=f"Failed to retrieve image. Status code: {response.status_code}")
                self.error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the error label over the canvas

        except Exception as e:
            # Display an error message if an exception occurs
            self.error_label.config(text=f"An error occurred: {str(e)}")
            self.error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the error label over the canvas
