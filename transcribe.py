import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def transcribe_audio(file_path):
    try:
        # Uploading the audio file to the Gemini API
        print(f"Uploading {file_path} for transcription...")
        audio_file = genai.upload_file(path=file_path)
        
        # Using Gemini 1.5 Flash for audio transcription
        model = genai.GenerativeModel("gemini-3-flash-preview")
        
        # Prompting Gemini to transcribe
        response = model.generate_content([
            "Please provide a highly accurate transcription of the following audio.",
            audio_file
        ])
        
        # Optionally, delete the file from the Google API server when done
        genai.delete_file(audio_file.name)
        
        return response.text

    except Exception as e:
        print(f"[API Error] {e}")
        print("⚠️ Falling back to local...")

        return local_transcribe(file_path)

# 🔥 LOCAL FALLBACK (very important for CV)
def local_transcribe(file_path):
    try:
        import whisper

        model = whisper.load_model("base")
        result = model.transcribe(file_path)

        return result["text"]

    except Exception as e:
        return f"[Fallback Error] {str(e)}"