# YouTube-Video-Notes-Generator
A Python-based application that converts YouTube videos into structured notes. It uses Whisper AI to process audio and generate English notes, with options for Hindi and Kannada translation and PDF downloads.

## Features

YouTube Audio Extraction: Downloads audio from YouTube videos.<br>
Speech-to-Text: Uses OpenAI Whisper to convert speech into English text.<br>
Notes Generation: Organizes the extracted text into summaries and key points.<br>
Multilingual Support: Provides options to translate notes into Hindi and Kannada.<br>
PDF Download: Allows users to download generated notes as PDF files.<br>
Interactive Interface: Built with Streamlit for a simple and user-friendly experience.<br>

## Technologies Used

Python<br>
Streamlit<br>
OpenAI Whisper<br>
yt-dlp<br>
FFmpeg<br>
Deep Translator<br>
ReportLab<br>

## How It Works

1. The user enters a YouTube video URL.<br>
2. The application extracts the video's audio using yt-dlp and FFmpeg.<br>
3. Whisper processes the audio and converts speech into English text.<br>
4. The extracted text is organized into structured notes.<br>
5. Notes can be translated into Hindi and Kannada.<br>
6. Users can view and download the notes in PDF format.<br>

## Application Screenshots

Home Page<br>
<img width="1012" height="522" alt="home" src="https://github.com/user-attachments/assets/1eb33f02-f98a-49d3-9ceb-6984e8d1aff2" width="200"/>

English Notes<br>
<img width="995" height="853" alt="english_notes" src="https://github.com/user-attachments/assets/83e442ec-7d21-4bdb-b2ce-0b05c9508195" width="200"/>

Kannada Notes<br>
<img width="992" height="855" alt="kannada_notes" src="https://github.com/user-attachments/assets/a86f32e8-6608-4de7-ba4b-6ef543e05645" width="200"/>

Hinidi Notes<br>
<img width="959" height="852" alt="hinidi_notes" src="https://github.com/user-attachments/assets/fd869b23-05ac-4923-923e-df6f0b4bc87e" width="200"/>

PDF Output
<img width="976" height="847" alt="downloaded_notes" src="https://github.com/user-attachments/assets/f8b7c7b8-c288-4351-a8f4-38a59a55bd94" width="200"/>



## Future Improvements

Improve translation reliability.<br>
Support additional languages.<br>
Enhance note summarization.<br>
Improve the user interface.<br>
