import tkinter as tk
import time
from datetime import datetime, timedelta
from image_local_loader import ImageLocalLoader
from video_player import VideoPlayer
from album_storage import AlbumStorage

root = tk.Tk()
root.title("Full Screen Image Viewer")

root.attributes("-fullscreen", True)
root.config(cursor="none")


albumsPath = "C:/Users/marca/source/repos/TimeReflect/Albums"
albumName = "album3"
pictureDisplaySeconds = 5

albums = AlbumStorage()
albumNames = albums.get_album_names(albumsPath)

oneAlbumPath = "/".join([albumsPath, albumName])
fileNames = albums.get_file_names(oneAlbumPath)


future_time = datetime.now()
current_time = datetime.now()

lastNdx = len(fileNames)
ndx = 0

def move():
    global ndx
    if(ndx == lastNdx):
        ndx = 0

    fileName = fileNames[ndx]
    isVideo = fileName.lower().endswith(".mp4")
    fileFullName = "/".join([albumsPath, albumName, fileName])

    if isVideo:
        video_player = VideoPlayer(root, fileFullName)
    else:
        image_loader = ImageLocalLoader(root)
        image_loader.load_image(fileFullName)

    ndx = ndx + 1

    root.after(3000, move) 

move()
root.mainloop()
        
