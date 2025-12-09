import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog, Scale, HORIZONTAL

class LineDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hough Transform Line Detection")
        
        self.label = Label(root, text="Select an Image for Line Detection")
        self.label.pack()
        
        self.select_button = Button(root, text="Choose Image", command=self.select_image)
        self.select_button.pack()
        
        self.canny_scale = Scale(root, from_=50, to=150, orient=HORIZONTAL, label='Canny Threshold')
        self.canny_scale.set(100)
        self.canny_scale.pack()