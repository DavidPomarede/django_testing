import cv2
import numpy as np
import imageio
import os

# Load the two images
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

# Define the number of frames in the animation
num_frames = 100

# Get the size of the images
height, width, _ = img1.shape

# Resize the images to the same size
img1 = cv2.resize(img1, (width, height))
img2 = cv2.resize(img2, (width, height))

# Create a list to store the frames
frames = []

# Define the morphing function
def morph(img1, img2, num_frames):
    for i in range(num_frames):
        # Calculate the alpha value for this frame
        alpha = i / (num_frames - 1)

        # Calculate the weighted sum of the two images
        frame = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)

        # Add the frame to the list
        frames.append(frame)

# Morph the two images
morph(img1, img2, num_frames)

# Save the frames to a GIF file
imageio.mimsave('morph.gif', frames, duration=0.05)

# Display the GIF animation
if os.name == 'nt':  # For Windows
    os.system('start morph.gif')
elif os.name == 'posix':  # For macOS and Linux
    os.system('open morph.gif')