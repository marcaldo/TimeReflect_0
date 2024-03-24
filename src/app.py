import tkinter as tk
from PIL import Image, ImageTk
from album_storage import AlbumStorage

# adjust window
root = tk.Tk()
root.geometry("1200x1200")

# Function to load images from file paths
def load_images(fileNames):
    images = []
    for fileName in fileNames:
        try:
            path = "/".join([albumsPath, albumName, fileName])
            image = ImageTk.PhotoImage(Image.open(path))
            images.append(image)
        except FileNotFoundError as e:
            print("Error loading image from", path, ":", e)
    return images


albumsPath = "C:/Users/marca/source/repos/TimeReflect/Albums"
albumName = "album2"
pictureDisplaySeconds = 2

albums = AlbumStorage()
albumNames = albums.get_album_names(albumsPath)

oneAlbumPath = "/".join([albumsPath, albumName])
fileNames = albums.get_file_names(oneAlbumPath)




# Load images
images = load_images(fileNames)

# create a label widget
label = tk.Label(root)
label.pack()

# Initialize index
index = 0

lastNdx = len(fileNames)
ndx = 0

def display():
    global ndx
    time_after = pictureDisplaySeconds * 1000
    if(ndx == lastNdx):
        ndx = 0

    # Display the next image
    label.config(image=images[ndx])
    # Increment index circularly
    ndx = ndx + 1
    # Call the move function again after 2000 milliseconds
    root.after(time_after, display)

# Call the move function to start the slideshow
display()

root.mainloop()
