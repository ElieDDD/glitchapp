import pandas
import numpy
import os
import random
from PIL import Image
from glitch_this import ImageGlitcher
import streamlit as st



def main():
    
    st.title('AI Forensics')
    st.text('Who benefits from the use of such images to train machine learning models?')
    #refresh = st.button("Refresh app")
    st.button("break another one")
    activities = ['Break', 'About']
    choice = st.sidebar.selectbox('Select Activity', activities)
    if choice == 'Break':
        st.subheader('Break images here, release them back into the wild')
        #imagefile = st.file_uploader('Upload Image', type=['jpg','png','jpeg'])
        #if imagefile is not None:
          # our_image =  Image.open(imagefile)
           #st.text('Original Image')
           #st.image(our_image)
    elif choice == 'About':
        st.subheader('About AI Forensics')
        st.markdown('Cambridge Digital Humanities [AI Forensics](https://elieddd.github.io/)')
        st.text('A project about large image data sets')
        
if __name__== '__main__':
    main()


 
    
    
def get_random_image_path(folder_path):
    try:
        files = os.listdir(folder_path)
        # Filter the list to get only image files
        images = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        if not images:
            #print("No images found in the specified folder.")
            return None

        # Choose a random image file
        random_image = random.choice(images)
        random_image_path = os.path.join(folder_path, random_image)
        return random_image_path
      
    except Exception as e:
        print(f"An error occurred while selecting image randomly: {e}")
        return None

def display_image(image_path):
    try:
        if image_path and os.path.isfile(image_path):
            with Image.open(image_path) as img:
                glitcher = ImageGlitcher()
                glitch_img = glitcher.glitch_image(img, 10, color_offset=True)
                #glitch_img.show()
                st.image(glitch_img,"", 500,)
            
                #print(f"Displayed image: {image_path}")
        else:
            print(f"Invalid image path: {image_path}")
    except Exception as e:
        print(f"An error occurred while displaying the image: {e}")

def show_random_image_from_folder(folder_path):
    random_image_path = get_random_image_path(folder_path)
    display_image(random_image_path)

# usage:
if __name__ == "__main__":
    folder_path = 'glics'
    if os.path.isdir(folder_path):
        show_random_image_from_folder(folder_path)
    else:
        print(f" The specified folder does not exist: {folder_path}")
