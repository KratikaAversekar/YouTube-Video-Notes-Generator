#translator.py

from deep_translator import GoogleTranslator
import time


def translate_text(text, target_lang):
    if not text or not text.strip():
        return ""

    try:
        # Split text into smaller chunks
        chunks = [
            text[i:i + 1000]
            for i in range(0, len(text), 1000)
        ]

        translator = GoogleTranslator(
            source="en",
            target=target_lang
        )

        # Retry translation if Google temporarily blocks requests
        for attempt in range(3):
            try:
                translated_chunks = translator.translate_batch(chunks)

                if not translated_chunks or any(
                    not item for item in translated_chunks
                ):
                    raise Exception("Google returned an empty translation.")

                return "\n".join(translated_chunks)

            except Exception as error:
                print(f"Translation attempt {attempt + 1} failed:", error)

                if attempt < 2:
                    time.sleep(10 * (attempt + 1))
                else:
                    raise error

    except Exception as e:
        print(f"Translation Error ({target_lang}):", e)
        return f"TRANSLATION_FAILED: {str(e)}"


# from deep_translator import GoogleTranslator
# import time


# def translate_text(text, target_lang):

#     if not text or not text.strip():
#         return ""

#     try:
#         chunks = [
#             text[i:i + 1500]
#             for i in range(0, len(text), 1500)
#         ]

#         translated_chunks = []

#         translator = GoogleTranslator(
#             source="en",
#             target=target_lang
#         )

#         for index, chunk in enumerate(chunks):

#             translated = translator.translate(chunk)

#             if not translated:
#                 raise Exception("Empty translation received")

#             translated_chunks.append(translated)

#             if index < len(chunks) - 1:
#                 time.sleep(2)

#         return "\n".join(translated_chunks)

#     except Exception as e:

#         print(f"Translation Error ({target_lang}):", e)

#         return f"TRANSLATION_FAILED: {str(e)}"


# from deep_translator import GoogleTranslator
# import time

# def translate_text(text, target_lang):
#     try:
#         if not text or text.strip() == "":
#             return text

#         text = text[:12000]
#         chunks = [
#             text[i:i + 2000]
#             for i in range(0, len(text), 2000)
#         ]

#         final_text = ""

#         for index, chunk in enumerate(chunks):
#             try:
#                 translated = GoogleTranslator(
#                     source="auto",
#                     target=target_lang
#                 ).translate(chunk)

#                 if translated:
#                     final_text += translated + "\n"
#                 else:
#                     print("Empty translation received")
#                     final_text += chunk + "\n"

#             except Exception as chunk_error:
#                 print("Chunk Error:", chunk_error)
#                 final_text += chunk + "\n"

#             # Pause between requests
#             if index < len(chunks) - 1:
#                 time.sleep(2)

#         return final_text.strip()

#     except Exception as e:
#         print("Translation Error:", e)
#         return text





# #translator.py
# from deep_translator import GoogleTranslator

# def translate_text(text, target_lang):
#     try:
#         # Handle empty input
#         if not text or text.strip() == "":
#             return text

#         # Limit size (prevents crashes)
#         text = text[:12000]

#         # Split into chunks (safe size)
#         chunks = [text[i:i+2000] for i in range(0, len(text), 2000)]

#         final_text = ""

#         for chunk in chunks:
#             try:
#                 translated = GoogleTranslator(
#                     source='auto',
#                     target=target_lang
#                 ).translate(chunk)

#                 # If translation fails, keep original chunk
#                 if translated:
#                     final_text += translated + "\n"
#                 else:
#                     final_text += chunk + "\n"

#             except Exception as chunk_error:
#                 print("Chunk Error:", chunk_error)
#                 final_text += chunk + "\n"

#         return final_text.strip()

#     except Exception as e:
#         print("Translation Error:", e)
#         return text   # fallback to English (VERY IMPORTANT)

# from deep_translator import GoogleTranslator

# def translate_text(text, target_lang):
#     try:
#         chunks = [text[i:i+3000] for i in range(0, len(text), 3000)]

#         final_text = ""

#         for chunk in chunks:
#             translated = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
#             final_text += translated + "\n"

#         return final_text

#     except Exception as e:
#         return f"Translation Error: {e}"

# from googletrans import Translator

# translator = Translator()

# def translate_text(text, target_lang):
#     try:
#         translated = translator.translate(text, dest=target_lang)
#         return translated.text
#     except Exception as e:
#         return f"Translation Error: {e}"