from google import genai
from dotenv import load_dotenv
from gtts import gTTS
from io import BytesIO
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Error with API key")

client = genai.Client(api_key=api_key)

def create_advanced_prompt(style):

    # --- Base prompt ---
    base_prompt = f"""
    Persona: You are a friendly storyteller who keeps things light and engaging.
    Goal: Write a story that is simple, clear, and fun to read.
    Task: Use all the given images to create one connected story.
    Genre: The story should follow the '{style}' style.
    
    Core Instructions:
    1. Tell one complete story with a beginning, middle, and end.
    2. Use at least one important detail from every image.
    3. Be creative in connecting the images together.
    4. Use only Indian names, characters, places, and cultural details.
    
    Output:
    - Title: Start with a short and clear title.
    - Length: The story should be 1 to 2 very small paragraphs.
    - Language: English (India)
    """

    # --- Style-specific instructions ---
    style_instruction = ""
    if style == "Morale":
        style_instruction = "\nSpecial Note: After the story, add [MORAL]: one simple sentence that shares the lesson of the story."
    elif style == "Mystery":
        style_instruction = "\nSpecial Note: After the story, add [SOLUTION]: reveal who the culprit was and the key clue that gave it away."
    elif style == "Thriller":
        style_instruction = "\nSpecial Note: After the story, add [TWIST]: a final shocking twist that changes everything."
    elif style == "Comedy":
        style_instruction = "\nSpecial Note: After the story, add [PUNCHLINE]: a funny or witty ending line that leaves the reader smiling."
    elif style == "Fairy Tale":
        style_instruction = "\nSpecial Note: After the story, add [HAPPILY EVER AFTER]: a short closing line that gives a magical or hopeful ending."
    elif style == "Sci-Fi":
        style_instruction = "\nSpecial Note: After the story, add [TECH DETAIL]: a short futuristic or scientific explanation that grounds the story in sci-fi."
    elif style == "Adventure":
        style_instruction = "\nSpecial Note: After the story, add [NEXT QUEST]: a hint about what exciting journey or challenge comes next."
    elif style == "Historical Fiction":
        style_instruction = "\nSpecial Note: After the story, add [HISTORICAL CONTEXT]: a short note about the real historical background that inspired the story."

    return base_prompt + style_instruction



def generate_story_with_images(images, style):

    response = client.models.generate_content(
        model= "gemini-2.5-flash-lite",
        contents=[images, create_advanced_prompt(style)],
    )
    
    return response.text

def narrate_story(story_text):

    try:
        tts= gTTS(text=story_text, lang="en-IN", slow=False)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp
    
    except Exception as e:
        return f"An unexpected error during the API call: {e}"