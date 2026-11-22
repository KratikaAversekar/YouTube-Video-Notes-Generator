#main.py
from utils.downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.translator import translate_text
import os


def format_notes(text):
    sentences = text.split(". ")

    formatted = "📘 SMART NOTES\n"
    formatted += "=" * 40 + "\n\n"

    summary = ". ".join(sentences[:5])
    formatted += "🔹 Quick Summary:\n"
    formatted += summary.strip() + ".\n\n"

    formatted += "🔹 Key Points:\n\n"

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 20:
            formatted += "• " + sentence + ".\n"

    return formatted


def main():
    print("\n🎥 NoteWise AI\n")

    url = input("Enter YouTube URL: ")

    print("\nDownloading audio...")
    audio_path = download_audio(url)

    print("Transcribing audio...")
    transcript = transcribe_audio(audio_path)

    print("Generating English notes...")
    english_notes = format_notes(transcript)

    print("Translating to Hindi...")
    hindi_notes = translate_text(english_notes, "hi")

    print("Translating to Kannada...")
    kannada_notes = translate_text(english_notes, "kn")

    # Save all
    with open("notes_english.txt", "w", encoding="utf-8") as f:
        f.write(english_notes)

    with open("notes_hindi.txt", "w", encoding="utf-8") as f:
        f.write(hindi_notes)

    with open("notes_kannada.txt", "w", encoding="utf-8") as f:
        f.write(kannada_notes)

    print("\n✅ Notes saved in 3 languages:")
    print("• notes_english.txt")
    print("• notes_hindi.txt")
    print("• notes_kannada.txt")


if __name__ == "__main__":
    main()

# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# import os


# def format_notes(text):
#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     # Summary
#     summary = ". ".join(sentences[:5])
#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if len(sentence) > 20:
#             formatted += "• " + sentence + ".\n"

#     return formatted


# def main():
#     print("\n🎥 NoteWise AI\n")

#     url = input("Enter YouTube URL: ")

#     print("\nDownloading audio...")
#     audio_path = download_audio(url)

#     print("Transcribing audio...")
#     transcript = transcribe_audio(audio_path)

#     print("Generating notes...")
#     notes = format_notes(transcript)

#     # Save notes
#     with open("final_notes.txt", "w", encoding="utf-8") as f:
#         f.write(notes)

#     print("\n✅ Notes saved to final_notes.txt")


# if __name__ == "__main__":
#     main()

# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# import os

# def format_notes(text):
#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     # Add short summary (first 5 sentences)
#     summary = ". ".join(sentences[:5])
#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if len(sentence) > 20:
#             formatted += "• " + sentence + ".\n"

#     return formatted

# def format_notes(text):
#     # Split into sentences
#     sentences = text.split(". ")

#     formatted = "\n📘 Generated Notes\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if sentence:
#             formatted += "• " + sentence + ".\n"

#     return formatted


def main():
    # Step 1: Ask YouTube URL
    url = input("Enter YouTube URL: ").strip()

    # Step 2: Download audio
    audio_path = download_audio(url)
    print("Audio downloaded at:", audio_path)

    # Step 3: Transcribe
    transcript = transcribe_audio(audio_path)

    # Step 4: Format notes
    formatted_notes = format_notes(transcript)

    # Step 5: Save to file
    output_file = "notes.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(formatted_notes)

    print("\n✅ Transcript saved to notes.txt")


if __name__ == "__main__":
    main()

# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# import os

# # Step 1: Ask for YouTube URL
# url = input("Enter YouTube URL: ").strip()

# # Step 2: Download audio
# audio_path = download_audio(url)
# print("Audio downloaded at:", audio_path)

# # Step 3: Transcribe
# transcript = transcribe_audio(audio_path)

# # Step 4: Save transcript
# output_file = "notes.txt"
# with open(output_file, "w", encoding="utf-8") as f:
#     f.write(transcript)

# print("\n✅ Transcript saved to notes.txt")