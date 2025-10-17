import streamlit as st
from io import BytesIO
from PIL import Image

from story_generator import generate_story_with_images, narrate_story

st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("📖 AI Story Generator")
st.markdown(">Upload 1–10 images, choose a style, and let AI write and narrate your story.")

with st.sidebar:

    st.title("Controls")

    # image uploader
    uploaded_files = st.file_uploader(
        "Upload files here:",
        type=['png', 'jpeg', 'jpg'],
        accept_multiple_files=True
    )
    
    # story style
    story_style = st.selectbox(
        "Select the story style",
        ('Comedy', 'Thriller', 'Fairy Tale', 'Sci-FI', 'Mystery', 'Adventure', 'Morale', "Historical Fiction")
    )


# Preview uploaded images
if uploaded_files:
    st.subheader("Preview")

    pil_images = []
    image_columns = st.columns(len(uploaded_files))

    for i, file in enumerate(uploaded_files):
        # Open the image
        img = Image.open(file)
        pil_images.append(img)

        # Reset the file pointer so it can be read again later
        file.seek(0)

        # Display in its column
        with image_columns[i]:
            st.image(img, caption=file.name, use_container_width=True)


# button to generate story
generate_button = st.button("Generate the Story", type="primary")



if generate_button:

    if not uploaded_files:
        st.warning("⚠️ Please add at least one image before proceeding")
    elif len(uploaded_files)>10:
        st.warning("⚠️ Please upload no more than 10 images")
    else:
        try:
            with st.spinner("Your story is coming to life with words and voice…"):

                # generate story
                generating_story = generate_story_with_images(pil_images, story_style)
                if generating_story:
                    st.header(f"Your {story_style} story: ")
                    st.success(generating_story)
                
            with st.spinner("We are half way, almost ready ✨"):

                # generte audio
                generating_audio = narrate_story(generating_story)
                if generating_audio:
                    st.header(f"Listen to Your Story")
                    st.audio(generating_audio, format="audio/mp3")
                    
        except Exception as e:
            st.error(f"Unexpected error: {e}")
