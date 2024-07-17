import streamlit as st
from itertools import cycle
from PIL import Image
import os

# Set the page layout to wide and the sidebar to always be open
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Set the title of the Streamlit app
st.title("IMAGE TABLE")

# Path to the folder containing images
image_folder = "img"

# Load images from the folder
filteredImages = []

for filename in os.listdir(image_folder):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        img_path = os.path.join(image_folder, filename)
        image = Image.open(img_path)
        filteredImages.append(image)

# Initialize session state for like statuses and liked images
if 'likes' not in st.session_state:
    st.session_state.likes = [False] * len(filteredImages)
if 'liked_images' not in st.session_state:
    st.session_state.liked_images = []

# Function to toggle like status
def toggle_like(index):
    st.session_state.likes[index] = not st.session_state.likes[index]
    if st.session_state.likes[index]:
        st.session_state.liked_images.append(index)
    else:
        st.session_state.liked_images.remove(index)

# Sidebar content
with st.sidebar:
    st.text_area("Enter prompt", height=200)
    st.button("Generate")
    st.header("Liked Images")
    for idx in st.session_state.liked_images:
        st.image(filteredImages[idx], width=200)  # Display smaller version of liked images

# Display images in a grid format without captions within a full-width container
with st.container():
    cols = cycle(st.columns(3))  # Create a cycle of columns for a 3-column layout
    for idx, filteredImage in enumerate(filteredImages):
        col = next(cols)
        col.image(filteredImage, width=300)  # Adjust width to make images larger
        # Display like/unlike button
        if st.session_state.likes[idx]:
            col.button("Unlike", type='primary', key=f"unlike_{idx}", on_click=toggle_like, args=(idx,))
        else:
            col.button("Like", key=f"like_{idx}", on_click=toggle_like, args=(idx,))
