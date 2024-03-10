import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root, video_path):
        self.root = root
        self.canvas = tk.Canvas(root)
        self.canvas.pack()
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        # self.canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack(fill=tk.BOTH, expand=True, side=tk.TOP)  # Fill the entire window and position at the top
        self.canvas.lift(self.root)
        self.play_video()

    def play_video(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Convert the frame to RGB format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Resize the frame to fit the canvas
                height, width = frame.shape[:2]
                ratio = min(self.root.winfo_screenwidth() / width, self.root.winfo_screenheight() / height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                frame = cv2.resize(frame, (new_width, new_height))
                 # Calculate coordinates to center the video on the canvas
                x = (self.canvas.winfo_width() - new_width) // 2
                y = (self.canvas.winfo_height() - new_height) // 2
                # Convert the frame to a format that PIL can display
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)
                # Display the frame on the canvas
                self.canvas.create_image(x, y, anchor=tk.NW, image=photo)
                self.canvas.image = photo
            self.root.after(30, self.play_video)
        else:
            print("Error: Could not open video file.")
