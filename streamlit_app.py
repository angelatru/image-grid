import streamlit as st
from itertools import cycle
from PIL import Image
import os

# Set page to full-width of screen
st.set_page_config(layout="wide")

# Set the title of the Streamlit app
st.title("IMAGE TABLE")

# Path to the folder containing images
image_folder = "img"

# Load images and captions from the folder
filteredImages = []
captions = []

for filename in os.listdir(image_folder):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        img_path = os.path.join(image_folder, filename)
        image = Image.open(img_path)
        filteredImages.append(image)
        captions.append(os.path.splitext(filename)[0])  # Use filename without extension as caption

# Display images in a grid format with captions
cols = cycle(st.columns(4))  # Create a cycle of columns for a 4-column layout
for idx, filteredImage in enumerate(filteredImages):
    next(cols).image(filteredImage, width=300, caption=captions[idx])
