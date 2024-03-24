import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ExifTags
from album_storage import AlbumStorage

# adjust window
root = tk.Tk()
root.attributes('-fullscreen', True) 
root.config(cursor='none', bg='black')  

albumsPath = "C:/Users/marca/source/repos/TimeReflect/Albums"
albumName = "albumRotate"
# albumsPath = "G:/My Drive"
# albumName = "PhotoFrame"
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

            image = RotateImage(image)
            image = ResizeImage(image)

            # Add text overlay
            text = "Your Text Here"  # Change this to your desired text
            image_with_text = overlay_text(image, text, font)
            
            photo = ImageTk.PhotoImage(image_with_text)
            images.append(photo)

        except FileNotFoundError as e:
            print("Error loading image from", path, ":", e)
    return images

def ResizeImage(image):
    window_height = root.winfo_screenheight()
    img_width, img_height = image.size
    new_height = int(window_height)
    new_width = int(img_width * (new_height / img_height))
    image = image.resize((new_width, new_height))
    return image

def RotateImage(image):
    # Check if the image is sideways (rotated)
    try:
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
    except Exception:
        pass
    return image

# Load font for the text
font_size = 50
font = ImageFont.truetype("arial.ttf", font_size)

def overlay_text(image, text, font): 
    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    text_position = (10, 10)  # Position at top-left corner with 10 pixels padding
    draw.text(text_position, text, fill="white", font=font)
    return Image.alpha_composite(image.convert('RGBA'), overlay)




# Load images
images = load_images(fileNames)

# create a label widget
label = tk.Label(root, bg='black')
label.pack()

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
