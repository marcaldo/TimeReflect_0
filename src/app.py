import tkinter as tk
from image_local_loader import ImageLocalLoader
from video_player import VideoPlayer

root = tk.Tk()
root.title("Full Screen Image Viewer")

root.attributes("-fullscreen", True)
root.config(cursor="none")

# fileName = "C:/Users/marca/source/repos/TimeReflect/Pictures/dragon.mp4"
fileName = "C:/Users/marca/source/repos/TimeReflect/Pictures/vertical.jpg"

isVideo = fileName.lower().endswith(".mp4")

if isVideo:
    video_player = VideoPlayer(root, fileName)
else:
    image_loader = ImageLocalLoader(root)
    image_loader.load_image(fileName)


# Run the Tkinter event loop
root.mainloop()
