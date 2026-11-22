# YouTube-Video-Notes-Generator
A Python-based application that converts YouTube videos into structured notes. It uses Whisper AI to process audio and generate English notes, with options for Hindi and Kannada translation and PDF downloads.

Features

YouTube Audio Extraction: Downloads audio from YouTube videos.<br>
Speech-to-Text: Uses OpenAI Whisper to convert speech into English text.<br>
Notes Generation: Organizes the extracted text into summaries and key points.<br>
Multilingual Support: Provides options to translate notes into Hindi and Kannada.<br>
PDF Download: Allows users to download generated notes as PDF files.<br>
Interactive Interface: Built with Streamlit for a simple and user-friendly experience.<br>

Technologies Used

Python<br>
Streamlit<br>
OpenAI Whisper<br>
yt-dlp<br>
FFmpeg<br>
Deep Translator<br>
ReportLab<br>

How It Works

1. The user enters a YouTube video URL.<br>
2. The application extracts the video's audio using yt-dlp and FFmpeg.<br>
3. Whisper processes the audio and converts speech into English text.<br>
4. The extracted text is organized into structured notes.<br>
5. Notes can be translated into Hindi and Kannada.<br>
6. Users can view and download the notes in PDF format.<br>
