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
albumName = "album 2"
# fileName = ""
pictureDisplaySeconds = 5

albums = AlbumStorage()
albumNames = albums.get_album_names(albumsPath)

oneAlbumPath = "/".join([albumsPath, albumName])
fileNames = albums.get_file_names(oneAlbumPath)


future_time = datetime.now()

image_loader = ImageLocalLoader(root)

# idx = 0

def load_picture(idx):
# def load_picture(loader, idx):
    # for fileName in fileNames:
        
        # if(idx > 0):
        #     loader.canvas.delete("all")

        fileName = fileNames[idx]
        isVideo = fileName.lower().endswith(".mp4")
        fileFullName = "/".join([albumsPath, albumName, fileName])

        # current_time = datetime.now()
        # if(current_time >= future_time):
        #     print(fileFullName)
        #     future_time = datetime.now() + timedelta(seconds=pictureDisplaySeconds)

        if isVideo:
            video_player = VideoPlayer(root, fileFullName)
        else:
            ing_loader = ImageLocalLoader(root)
            ing_loader.load_image(fileFullName)

        idx = idx + 1

        if(idx > 2):
            idx = 0

        # root.after(3000, load_picture, loader, idx)
        root.after(3000, load_picture, idx)

# load_picture(image_loader, 0)
load_picture(0)

root.mainloop()



# while(True):
#     for fileName in fileNames:
#         isVideo = fileName.lower().endswith(".mp4")
#         fileFullName = "/".join([albumsPath, albumName, fileName])

#         if isVideo:
#             video_player = VideoPlayer(root, fileFullName)
#         else:
#             image_loader = ImageLocalLoader(root)
#             image_loader.load_image(fileFullName)
#         # print(fileFullName)
            


# Run the Tkinter event loop
    # root.mainloop()


# def print_file_names(fileName, pictureDisplayTime):
#     future_time = datetime.now() + timedelta(seconds=pictureDisplayTime)
#     while True:
#         current_time = datetime.now()
#         if current_time >= future_time:
#             print("File name:", fileName)
#         time.sleep(1)


