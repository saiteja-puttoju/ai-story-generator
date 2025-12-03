# 📖 AI Story Generator with Images

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai-story-generator-by-saiteja-puttoju.streamlit.app/)
[![Read on Hashnode](https://img.shields.io/badge/Hashnode-Read%20Blog%20Post-2962FF?style=for-the-badge&logo=hashnode&logoColor=white)](https://saitejaputtoju.hashnode.dev/ai-story-generator)
[![Watch Demo](https://img.shields.io/badge/YouTube-Watch%20Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/YMYFy5cUx6c?si=Og61TbCdNt6BfaxE)


An interactive web application built with Streamlit that uses Google's Gemini Pro Vision to generate a unique, short story based on a series of user-uploaded images. The application also provides an audio narration of the generated story.

-----

## 🌟 Key Features

  * **Image-to-Story:** Upload between 1 and 10 images to serve as the creative inspiration for the story.
  * **Genre Selection:** Choose from a variety of story styles, including Comedy, Thriller, Fairy Tale, Sci-Fi, and more, to guide the AI's tone and narrative.
  * **Custom Instructions:** An optional text box allows you to add specific instructions (e.g., "Make it funny," "Set the output language") to further personalize the story.
  * **Dynamic Prompting:** The backend uses an advanced prompting strategy that adapts based on the selected genre and user instructions.
  * **Audio Narration:** Listen to your generated story with an integrated audio player, powered by Google Text-to-Speech (gTTS).
  * **Indian Context:** The AI is instructed to use Indian names, characters, and cultural details, giving the stories a distinct flavor.
  * **Interactive UI:** A simple and intuitive user interface built with Streamlit allows for easy image uploads and controls.

-----

## 🛠️ Technologies Used

  * **Backend:** Python
  * **AI Model:** Google Gemini Pro Vision
  * **Web Framework:** Streamlit
  * **Text-to-Speech:** gTTS (Google Text-to-Speech)
  * **Dependencies:**
      * `google-generativeai`
      * `python-dotenv`
      * `Pillow`

-----

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

  * Python 3.12 or later
  * A Google API Key with the Gemini API enabled. You can get one from [Google AI Studio](https://makersuite.google.com/).

### Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/saiteja-puttoju/ai-story-generator.git
    cd ai-story-generator
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # For Linux/macOS
    python -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**

      * Create a new file in the root of the project named `.env`.
      * Add your Google API key to this file as shown below:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

### Running the Application

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run app.py
```

Your web browser will automatically open to the application's user interface.

-----

## How to Use

1.  **Upload Images:** Use the file uploader in the sidebar to select and upload 1 to 10 images (`.png`, `.jpeg`, `.jpg`).
2.  **Select a Style:** Choose your desired story genre from the dropdown menu.
3.  **Add Instructions (Optional):** Use the text box to add any extra directions for the AI.
4.  **Generate:** Click the **"Generate Story and Narration"** button.
5.  **Enjoy:** The application will display the generated story text and provide an audio player to listen to the narration.
