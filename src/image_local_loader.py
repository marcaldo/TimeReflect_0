import tkinter as tk
from PIL import Image, ImageTk

class ImageLocalLoader:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg="black", borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
    
    def load_image(self, image_path):
        try:
            self.canvas.delete(tk.ALL) 

            image = Image.open(image_path)

            window_width = self.root.winfo_screenwidth()
            window_height = self.root.winfo_screenheight()

            img_width, img_height = image.size
            new_height = int(window_height)
            new_width = int(img_width * (new_height / img_height))
            image = image.resize((new_width, new_height))

            x = (window_width - image.width) // 2
            y = (window_height - image.height) // 2


            photo = ImageTk.PhotoImage(image)

            # print(str(image.width) + ", " + str(image.height))
            # print(str(x) + ", " + str(y))

            self.canvas.create_image(x, y, anchor=tk.NW, image=photo)

            # Keep a reference to the photo to prevent garbage collection
            self.canvas.image = photo


        except Exception as e:
            # Display an error message if an exception occurs
            # self.error_label = tk.Label(self, fg="red", text="")
            #self.error_label.pack()
            self.error_label.config(text=f"An error occurred: {str(e)}")
            self.error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Position the error label over the canvas
