import tkinter as tk
from image_loader import ImageLoader

# Create the Tkinter window
root = tk.Tk()
root.title("Full Screen Image Viewer")

# Configure the window to be full screen
root.attributes("-fullscreen", True)
root.configure(bg="black")  # Set background color to black to match the image background

# Set border width to 0 and remove padding
root.attributes("-fullscreen", True)
root.attributes("-fullscreen", True)
root.configure(bg="black")

# Create an instance of ImageLoader
image_loader = ImageLoader(root)

# Load the image
image_loader.load_image("https://images.stockcake.com/public/0/9/6/096537ac-2343-4187-b150-e2fa00120af8/autumn-lake-view-stockcake.jpg")

# Run the Tkinter event loop
root.mainloop()
