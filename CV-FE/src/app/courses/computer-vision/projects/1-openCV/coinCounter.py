import cv2
import numpy
import argparse
import os



imgPath=""
image= cv2.imread("https://github.com/swapnilxi/A-computer-vision/blob/open-cv-projects/40daysCV/frontend/src/app/courses/computer-vision/projects/ImagesData/coinImage.jpg")

def process_images(image, blur_kernel_size, threshold_value, erosion_iterations, final_threshold_value):
#converting to grayscale 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#applying gaussian blur - it should be odd
    if blur_kernel_size % 2 == 0:
        blur_kernel_size += 1
    blurred = cv2.GaussianBlur(gray, (blur_kernel_size, blur_kernel_size), 0)
#applying thresholding for des

    _, binary_image = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY)


#applying more blur
    
    