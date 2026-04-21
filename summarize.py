import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_text(text):
    if not text or text.strip() == "":
        return "No content to summarize."

    try:
        model = genai.GenerativeModel("gemini-3-flash-preview")
        
        prompt = f"""
Summarize the following transcript and return:

1. Translate the audio into English if the audio is of another another language
2. Short summary (max 4 sentences)
3. Key points (bullet points)
4. Action items (if any)
5. Important quotes (if any)

Transcript:
{text}
"""
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"[Summarization Error] {str(e)}"