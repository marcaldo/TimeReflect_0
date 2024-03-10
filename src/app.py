import tkinter as tk
import os
from image_local_loader import ImageLocalLoader
from video_player import VideoPlayer

root = tk.Tk()
root.title("Full Screen Image Viewer")

root.attributes("-fullscreen", True)
root.config(cursor="none")

albumsPath = "C:/Users/marca/source/repos/TimeReflect/Albums"
albumName = "album1"
fileName = "dragon.MP4"

# script_dir = os.path.dirname(__file__)
# two_levels_up_dir = os.path.dirname(script_dir)

isVideo = fileName.lower().endswith(".mp4")

fileFullName = "/".join([albumsPath, albumName, fileName])

if isVideo:
    video_player = VideoPlayer(root, fileFullName)
else:
    image_loader = ImageLocalLoader(root)
    image_loader.load_image(fileFullName)


# Run the Tkinter event loop
root.mainloop()


