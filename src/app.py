import tkinter as tk
from image_local_loader import ImageLocalLoader
from video_player import VideoPlayer

# Create the Tkinter window
root = tk.Tk()
root.title("Full Screen Image Viewer")

# Configure the window to be full screen
root.attributes("-fullscreen", True)
root.config(cursor="none")
# root.configure(bg="black")  # Set background color to black to match the image background

# # Set border width to 0 and remove padding
# root.attributes("-fullscreen", True)
# root.attributes("-fullscreen", True)
# root.configure(bg="black")

isVideo = False

if isVideo:
    video_player = VideoPlayer(root, "C:/Users/marca/source/repos/TimeReflect/Pictures/dragon.mp4")
else:
    image_loader = ImageLocalLoader(root)
    image_loader.load_image("C:/Users/marca/source/repos/TimeReflect/Pictures/superior.jpg")


# Load the image
# image_loader.load_image("https://images.stockcake.com/public/0/9/6/096537ac-2343-4187-b150-e2fa00120af8/autumn-lake-view-stockcake.jpg")
# image_loader.load_image("C:/Users/marca/source/repos/TimeReflect/Pictures/20180620_152359.jpg")


# Run the Tkinter event loop
root.mainloop()
