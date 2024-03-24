import tkinter as tk
from PIL import Image, ImageTk, ExifTags
from album_storage import AlbumStorage

# adjust window
root = tk.Tk()
root.attributes('-fullscreen', True) 
root.config(cursor='none', bg='black')  

albumsPath = "C:/Users/marca/source/repos/TimeReflect/Albums"
albumName = "album2"
pictureDisplaySeconds = 2

albums = AlbumStorage()
albumNames = albums.get_album_names(albumsPath)

oneAlbumPath = "/".join([albumsPath, albumName])
fileNames = albums.get_file_names(oneAlbumPath)


# Function to load images from file paths
def load_images(fileNames):
    images = []
    for fileName in fileNames:
        try:
            path = "/".join([albumsPath, albumName, fileName])
            image = Image.open(path)


            # Check if the image is sideways (rotated)
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(image._getexif().items())

            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)


            window_height = root.winfo_screenheight()
            img_width, img_height = image.size
            new_height = int(window_height)
            new_width = int(img_width * (new_height / img_height))
            image = image.resize((new_width, new_height))

            photo = ImageTk.PhotoImage(image)

            images.append(photo)
        except FileNotFoundError as e:
            print("Error loading image from", path, ":", e)
    return images


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
