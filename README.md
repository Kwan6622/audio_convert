🎙️ Audio Convert: AI Transcriber & Summarizer

Audio Convert is a streamlined web application that transforms audio files into readable text and concise AI-generated summaries. Built with Python and Streamlit, it provides a clean, user-friendly interface for processing lectures, meetings, or voice memos.

🚀 Features 

File Upload: Supports .mp3 and .wav audio formats.

Automated Transcription: High-accuracy conversion of speech to text.

AI Summarization: Distills long transcripts into key points using Natural Language Processing. (Using Gemini3-flash-review)

Dual-View Interface: Compare the full transcript and summary side-by-side using a tabbed UI.

One-Click Export: Download your generated summary directly as a text file.

🛠️ Tech Stack 

Frontend: Streamlit (Python-based Web Framework)

AI/ML: Custom modules for transcribe and summarize (Using Gemini API)

Environment: python-dotenv for secure API management

Language: Python 3.x

🔧 Installation & Setup

1. Clone the repository:

git clone https://github.com/Kwan6622/audio_convert.git

cd audio_convert

2. Install dependencies:

pip install streamlit python-dotenv

3. Configure Environment:

Create a .env file in the root directory and add your API credentials:

4. Run the App:

streamlit run app.py

🖥️ How it Works 

Injest: The user uploads an audio file which is temporarily buffered.

Process: The transcribe_audio function processes the binary data into a text string.

Summarize: The summarize_text function uses an LLM to generate a concise version of the transcript.

Output: The UI dynamically renders tabs for viewing and a button for downloading the final result.

# Example keys

GEMINI_API_KEY=your_api_key_here