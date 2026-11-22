#summarizer.py
import re

def generate_notes(transcript):

    sentences = re.split(r'[.!?]', transcript)

    notes = []
    for s in sentences:
        s = s.strip()
        if len(s) > 40:
            notes.append("• " + s.capitalize())

    clean_notes = "\n".join(notes)

    return "KEY POINTS\n\n" + clean_notes

# def generate_notes(transcript):
    
#     sentences = transcript.split(". ")

#     notes = []

#     for s in sentences:
#         s = s.strip()
#         if len(s) > 30:
#             notes.append("• " + s)

#     return "\n".join(notes)

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=api_key)

# def generate_notes(transcript):

#     prompt = f"""
#     Convert the following transcript into clean bullet-point notes in English.

#     Transcript:
#     {transcript}
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )

#     return response.choices[0].message.content