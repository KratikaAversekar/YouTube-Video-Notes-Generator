#transcriber.py
import whisper
import os

model = whisper.load_model("tiny")
# model = whisper.load_model("base")

def transcribe_audio(audio_path):

    audio_path = audio_path.strip().strip('"')
    audio_path = os.path.abspath(audio_path)

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"File not found: {audio_path}")

    result = model.transcribe(
        audio_path,
        task="translate"   # VERY IMPORTANT
    )

    return result["text"]


#  import whisper
# import os

# model = whisper.load_model("tiny")

# def transcribe_audio(audio_path):

#     audio_path = audio_path.strip().strip('"')
#     audio_path = os.path.abspath(audio_path)

#     if not os.path.exists(audio_path):
#         raise FileNotFoundError(f"File not found: {audio_path}")

#     result = model.transcribe(
#         audio_path,
#         task="translate"  # converts Hindi → English
#     )

#     return result["text"]


# import whisper
# import os

# def transcribe_audio(audio_path):

#     # Clean the path
#     audio_path = audio_path.strip().strip('"')
#     audio_path = os.path.abspath(audio_path)

#     if not os.path.exists(audio_path):
#         raise FileNotFoundError(f"File not found: {audio_path}")

#     # Load whisper model
#     model = whisper.load_model("base")

#     # Transcribe and translate to English
#     result = model.transcribe(
#         audio_path,
#         task="translate",
#         language=None
#     )

#     return result["text"]

# import whisper
# import os

# def transcribe_audio(audio_path):

#     # Clean path
#     audio_path = audio_path.strip().strip('"')
#     audio_path = os.path.abspath(audio_path)

#     if not os.path.exists(audio_path):
#         raise FileNotFoundError(f"File not found: {audio_path}")

#     # Load Whisper model
#     model = whisper.load_model("base")

#     # Translate any language to English
#     result = model.transcribe(audio_path, task="translate")

#     return result["text"]

# import whisper
# import os

# def transcribe_audio(audio_path):
#     # Clean path
#     audio_path = audio_path.strip().strip('"')
#     audio_path = os.path.abspath(audio_path)

#     if not os.path.exists(audio_path):
#         raise FileNotFoundError(f"File not found: {audio_path}")

#     print("Transcribing... (this may take a few minutes)")

#     # Load Whisper model
#     model = whisper.load_model("base")

#     # Transcribe audio
#     result = model.transcribe(audio_path)

#     return result["text"]

# import whisper
# import os

# def transcribe_audio(audio_path):
#     audio_path = audio_path.strip().strip('"')
#     audio_path = os.path.abspath(audio_path)

#     if not os.path.exists(audio_path):
#         raise FileNotFoundError(f"File not found: {audio_path}")

#     model = whisper.load_model("base")
#     result = model.transcribe(audio_path)

#     return result["text"]

# import whisper
# import os

# def transcribe_audio(audio_path):
#     # Clean the path properly
#     audio_path = audio_path.strip()
#     audio_path = os.path.abspath(audio_path)

#     # Debug prints (you can remove later)
#     print("Using audio path:", audio_path)

#     # Check if file exists
#     if not os.path.exists(audio_path):
#         raise FileNotFoundError(f"File not found: {audio_path}")

#     # Load model (first time will download model)
#     model = whisper.load_model("base")

#     # Transcribe
#     result = model.transcribe(audio_path)

#     return result["text"]

# import whisper

# # Load model only once (important)
# model = whisper.load_model("base")  
# # You can use "tiny" for faster, "small" for better accuracy

# def transcribe_audio(audio_path):
#     """
#     Takes audio file path
#     Returns transcript text
#     """
#     result = model.transcribe(audio_path)
#     transcript = result["text"]
#     return transcript