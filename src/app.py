import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_image():
    try:
        error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Make a GET request to the API endpoint that returns the image
        response = requests.get("https://images.stockcake.com/public/0/9/6/096537ac-2343-4187-b150-e2fa00120af8/autumn-lake-view-stockcake.jpg")
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the image from the response content
            image = Image.open(BytesIO(response.content))
            # Resize the image to fit the screen size
            width, height = root.winfo_screenwidth(), root.winfo_screenheight()
            image = image.resize((width, height))
            # Convert the image to a format that Tkinter can display
            photo = ImageTk.PhotoImage(image)
            # Display the image on the canvas
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            # Keep a reference to the photo to prevent garbage collection
            canvas.image = photo
            
            # Create a label on top of the canvas
            # label = tk.Label(root, text="", bg="white", highlightthickness=0)
            # label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Position the label in the center of the screen, 10% from the top

        else:
            # Display an error message if the request was unsuccessful
            error_label.config(text=f"Failed to retrieve image. Status code: {response.status_code}")
            # Position the error label over the canvas
            error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    except Exception as e:
        # Display an error message if an exception occurs
        error_label.config(text=f"An error occurred: {str(e)}")
        error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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


# Create a canvas to display the image
canvas = tk.Canvas(root, borderwidth=0, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Create a label to display error messages
error_label = tk.Label(root, fg="black")
# Position the error label over the canvas
error_label.place_forget()
error_label.pack()


# Load the image automatically when the application starts
get_image()

# Run the Tkinter event loop
root.mainloop()
