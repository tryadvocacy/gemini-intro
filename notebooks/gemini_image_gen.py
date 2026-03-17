
import google.generativeai as genai
from google.generativeai import types
from PIL import Image
import io
import os

# Configure the API key
gemini_api_key = os.environ.get("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")
genai.configure(api_key=gemini_api_key)

# Choose the image generation model
model = genai.GenerativeModel('gemini-2.5-flash-image')

# Define the prompt
prompt = "A futuristic city with flying cars"

print(f"Generating image for prompt: '{prompt}'...")

try:
    # Generate the image
    response = model.generate_content(prompt)

    # Check if the response has image data
    if response.candidates:
        for candidate in response.candidates:
            for part in candidate.content.parts:
                if part.inline_data and part.inline_data.mime_type.startswith('image/'):
                    image_data = part.inline_data.data
                    image = Image.open(io.BytesIO(image_data))
                    
                    # Save the image
                    image_filename = "generated_image.png"
                    image.save(image_filename)
                    print(f"Image saved as {image_filename}")
                    break
            break
    else:
        print("No image data found in the response.")

except Exception as e:
    print(f"An error occurred: {e}")
