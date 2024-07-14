import streamlit as st
from itertools import cycle
from PIL import Image
import os

# Set the page layout to wide
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

# Initialize session state for like statuses and liked images
if 'likes' not in st.session_state:
    st.session_state.likes = [False] * len(filteredImages)
if 'liked_images' not in st.session_state:
    st.session_state.liked_images = []

# Function to toggle like status
def toggle_like(index):
    st.session_state.likes[index] = not st.session_state.likes[index]
    if st.session_state.likes[index]:
        st.session_state.liked_images.append(captions[index])
    else:
        st.session_state.liked_images.remove(captions[index])

# Display images in a grid format with captions within a full-width container
with st.container():
    cols = cycle(st.columns(4))  # Create a cycle of columns for a 4-column layout
    for idx, filteredImage in enumerate(filteredImages):
        col = next(cols)
        col.image(filteredImage, width=300, caption=captions[idx])  # Adjust width to make images larger
        # Display like/unlike button
        if st.session_state.likes[idx]:
            col.button("Unlike", type='primary', key=f"unlike_{idx}", on_click=toggle_like, args=(idx,))
        else:
            col.button("Like", key=f"like_{idx}", on_click=toggle_like, args=(idx,))

# Display liked images as a string
st.subheader("Liked Images")
liked_images_string = ", ".join(st.session_state.liked_images)
st.write(liked_images_string)
