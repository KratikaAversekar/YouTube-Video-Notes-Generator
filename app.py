
#app.py

import streamlit as st

from utils.downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.translator import translate_text
from utils.pdf_generator import create_pdf


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="YouTube Video Notes Generator",
    page_icon="🎥",
    layout="centered"
)


# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------

if "notes_generated" not in st.session_state:
    st.session_state.notes_generated = False

if "english_notes" not in st.session_state:
    st.session_state.english_notes = ""

if "hindi_notes" not in st.session_state:
    st.session_state.hindi_notes = ""

if "kannada_notes" not in st.session_state:
    st.session_state.kannada_notes = ""


# --------------------------------------------------
# NOTES FORMATTING FUNCTION
# --------------------------------------------------

def format_notes(text):

    sentences = text.split(". ")

    formatted = "📘 SMART NOTES\n"
    formatted += "=" * 40 + "\n\n"

    # Quick Summary
    summary = ". ".join(sentences[:5])

    formatted += "🔹 Quick Summary:\n"
    formatted += summary.strip() + ".\n\n"

    # Key Points
    formatted += "🔹 Key Points:\n\n"

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) > 20:
            formatted += "• " + sentence + ".\n"

    return formatted


# --------------------------------------------------
# APPLICATION TITLE
# --------------------------------------------------

st.title("🎥 YouTube Video Notes Generator")

st.write(
    "Generate smart notes from YouTube videos in multiple languages"
)


# --------------------------------------------------
# YOUTUBE URL INPUT
# --------------------------------------------------

url = st.text_input("Paste YouTube URL here")


# --------------------------------------------------
# GENERATE NOTES BUTTON
# --------------------------------------------------

if st.button("Generate Notes"):

    if not url.strip():

        st.warning("Please enter a YouTube URL")

    else:

        # Clear previous notes before generating new notes
        st.session_state.notes_generated = False

        try:

            # Step 1: Download Audio
            with st.spinner("Downloading audio..."):

                audio_path = download_audio(url)

            if not audio_path:

                st.error("Failed to download audio. Try another video.")
                st.stop()


            # Step 2: Transcribe Audio
            with st.spinner("Transcribing audio..."):

                transcript = transcribe_audio(audio_path)

            if not transcript:

                st.error("Transcription failed.")
                st.stop()


            # Step 3: Generate English Notes
            with st.spinner("Generating English notes..."):

                english_notes = format_notes(transcript)

            english_notes = english_notes[:8000]


            # Step 4: Translate to Hindi
            with st.spinner("Translating to Hindi..."):

                hindi_notes = translate_text(
                    english_notes,
                    "hi"
                )


            # Step 5: Translate to Kannada
            with st.spinner("Translating to Kannada..."):

                kannada_notes = translate_text(
                    english_notes,
                    "kn"
                )


            # Step 6: Store Notes in Session State

            st.session_state.english_notes = english_notes

            st.session_state.hindi_notes = hindi_notes

            st.session_state.kannada_notes = kannada_notes

            st.session_state.notes_generated = True

            st.success("Notes generation completed!")


        except Exception as e:

            st.error(f"Error: {e}")


# --------------------------------------------------
# DISPLAY NOTES AND PDF DOWNLOADS
# --------------------------------------------------

if st.session_state.notes_generated:

    st.success("Your notes are ready!")

    tab1, tab2, tab3 = st.tabs(
        ["English", "Hindi", "Kannada"]
    )


    # --------------------------------------------------
    # ENGLISH TAB
    # --------------------------------------------------

    with tab1:

        st.text_area(
            "English Notes",
            st.session_state.english_notes,
            height=300
        )

        english_pdf = create_pdf(
            st.session_state.english_notes
        )

        st.download_button(
            label="Download English PDF",
            data=english_pdf,
            file_name="notes_english.pdf",
            mime="application/pdf"
        )


    # --------------------------------------------------
    # HINDI TAB
    # --------------------------------------------------

    with tab2:

        if st.session_state.hindi_notes.startswith(
            "TRANSLATION_FAILED:"
        ):

            #st.error(
            #    "Hindi translation failed. Please try generating notes again."
            #)
            st.error(st.session_state.hindi_notes)

        else:

            st.text_area(
                "Hindi Notes",
                st.session_state.hindi_notes,
                height=300
            )

            hindi_pdf = create_pdf(
                st.session_state.hindi_notes
            )

            st.download_button(
                label="Download Hindi PDF",
                data=hindi_pdf,
                file_name="notes_hindi.pdf",
                mime="application/pdf"
            )


    # --------------------------------------------------
    # KANNADA TAB
    # --------------------------------------------------

    with tab3:

        if st.session_state.kannada_notes.startswith(
            "TRANSLATION_FAILED:"
        ):

            #st.error(
            #    "Kannada translation failed. Please try generating notes again."
            #)
            st.error(st.session_state.kannada_notes)

        else:

            st.text_area(
                "Kannada Notes",
                st.session_state.kannada_notes,
                height=300
            )

            kannada_pdf = create_pdf(
                st.session_state.kannada_notes
            )

            st.download_button(
                label="Download Kannada PDF",
                data=kannada_pdf,
                file_name="notes_kannada.pdf",
                mime="application/pdf"
            )


# import streamlit as st

# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# from utils.translator import translate_text
# from utils.pdf_generator import create_pdf


# # --------------------------------------------------
# # PAGE CONFIGURATION
# # --------------------------------------------------

# st.set_page_config(
#     page_title="YouTube Video Notes Generator",
#     page_icon="🎥",
#     layout="centered"
# )


# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------

# if "notes_generated" not in st.session_state:
#     st.session_state.notes_generated = False

# if "english_notes" not in st.session_state:
#     st.session_state.english_notes = ""

# if "hindi_notes" not in st.session_state:
#     st.session_state.hindi_notes = ""

# if "kannada_notes" not in st.session_state:
#     st.session_state.kannada_notes = ""


# # --------------------------------------------------
# # NOTES FORMATTING FUNCTION
# # --------------------------------------------------

# def format_notes(text):

#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     # Quick Summary
#     summary = ". ".join(sentences[:5])

#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     # Key Points
#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:

#         sentence = sentence.strip()

#         if len(sentence) > 20:
#             formatted += "• " + sentence + ".\n"

#     return formatted


# # --------------------------------------------------
# # APPLICATION TITLE
# # --------------------------------------------------

# st.title("🎥 YouTube Video Notes Generator")

# st.write(
#     "Generate smart notes from YouTube videos in multiple languages"
# )


# # --------------------------------------------------
# # YOUTUBE URL INPUT
# # --------------------------------------------------

# url = st.text_input("Paste YouTube URL here")


# # --------------------------------------------------
# # GENERATE NOTES BUTTON
# # --------------------------------------------------

# if st.button("Generate Notes"):

#     if url.strip() == "":

#         st.warning("Please enter a YouTube URL")

#     else:

#         # Reset previous notes while generating new ones
#         st.session_state.notes_generated = False

#         try:

#             # Step 1: Download Audio
#             with st.spinner("Downloading audio..."):

#                 audio_path = download_audio(url)

#             if not audio_path:

#                 st.error("❌ Failed to download audio. Try another video.")
#                 st.stop()


#             # Step 2: Transcribe Audio
#             with st.spinner("Transcribing audio..."):

#                 transcript = transcribe_audio(audio_path)

#             if not transcript:

#                 st.error("❌ Transcription failed.")
#                 st.stop()


#             # Step 3: Generate English Notes
#             with st.spinner("Generating English notes..."):

#                 english_notes = format_notes(transcript)

#             # Limit size for translation
#             english_notes = english_notes[:8000]


#             # Step 4: Translate to Hindi
#             with st.spinner("Translating to Hindi..."):

#                 hindi_notes = translate_text(
#                     english_notes,
#                     "hi"
#                 )


#             # Step 5: Translate to Kannada
#             with st.spinner("Translating to Kannada..."):

#                 kannada_notes = translate_text(
#                     english_notes,
#                     "kn"
#                 )


#             # Translation fallback
#             if not hindi_notes or "Error" in hindi_notes:

#                 hindi_notes = (
#                     "Translation failed. Showing English instead.\n\n"
#                     + english_notes
#                 )

#             if not kannada_notes or "Error" in kannada_notes:

#                 kannada_notes = (
#                     "Translation failed. Showing English instead.\n\n"
#                     + english_notes
#                 )


#             # Step 6: Save Notes in Session State
#             st.session_state.english_notes = english_notes

#             st.session_state.hindi_notes = hindi_notes

#             st.session_state.kannada_notes = kannada_notes

#             st.session_state.notes_generated = True

#             st.success("✅ Notes generated successfully!")


#         except Exception as e:

#             st.error(f"❌ Error: {e}")


# # --------------------------------------------------
# # DISPLAY NOTES AND PDF DOWNLOADS
# # --------------------------------------------------

# if st.session_state.notes_generated:

#     st.success("Your notes are ready!")

#     # Create three language tabs
#     tab1, tab2, tab3 = st.tabs(
#         ["English", "Hindi", "Kannada"]
#     )


#     # --------------------------------------------------
#     # ENGLISH TAB
#     # --------------------------------------------------

#     with tab1:

#         st.text_area(
#             "English Notes",
#             st.session_state.english_notes,
#             height=300
#         )

#         english_pdf = create_pdf(
#             st.session_state.english_notes
#         )

#         st.download_button(
#             label="📄 Download English PDF",
#             data=english_pdf,
#             file_name="notes_english.pdf",
#             mime="application/pdf"
#         )


#     # --------------------------------------------------
#     # HINDI TAB
#     # --------------------------------------------------

#     with tab2:

#         st.text_area(
#             "Hindi Notes",
#             st.session_state.hindi_notes,
#             height=300
#         )

#         hindi_pdf = create_pdf(
#             st.session_state.hindi_notes
#         )

#         st.download_button(
#             label="📄 Download Hindi PDF",
#             data=hindi_pdf,
#             file_name="notes_hindi.pdf",
#             mime="application/pdf"
#         )


#     # --------------------------------------------------
#     # KANNADA TAB
#     # --------------------------------------------------

#     with tab3:

#         st.text_area(
#             "Kannada Notes",
#             st.session_state.kannada_notes,
#             height=300
#         )

#         kannada_pdf = create_pdf(
#             st.session_state.kannada_notes
#         )

#         st.download_button(
#             label="📄 Download Kannada PDF",
#             data=kannada_pdf,
#             file_name="notes_kannada.pdf",
#             mime="application/pdf"
#         )


# #app.py
# import streamlit as st

# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# from utils.translator import translate_text
# from utils.pdf_generator import create_pdf


# def format_notes(text):
#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     # Quick Summary
#     summary = ". ".join(sentences[:5])
#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     # Key Points
#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()

#         if len(sentence) > 20:
#             formatted += "• " + sentence + ".\n"

#     return formatted


# # UI setup
# st.set_page_config(
#     page_title="YouTube Video Notes Generator",
#     layout="centered"
# )

# st.title("🎥 YouTube Video Notes Generator")

# st.write(
#     "Generate smart notes from YouTube videos in multiple languages"
# )


# # YouTube URL input
# url = st.text_input("Paste YouTube URL here")


# # Generate Notes button
# if st.button("Generate Notes"):

#     if url.strip() == "":
#         st.warning("Please enter a YouTube URL")

#     else:
#         try:

#             # Step 1: Download audio
#             with st.spinner("Downloading audio..."):
#                 audio_path = download_audio(url)

#             if not audio_path:
#                 st.error("❌ Failed to download audio. Try another video.")
#                 st.stop()

#             # Step 2: Transcribe audio
#             with st.spinner("Transcribing audio..."):
#                 transcript = transcribe_audio(audio_path)

#             if not transcript:
#                 st.error("❌ Transcription failed.")
#                 st.stop()

#             # Step 3: Generate English notes
#             with st.spinner("Generating notes..."):
#                 english_notes = format_notes(transcript)

#             # Limit size for translation
#             english_notes = english_notes[:8000]

#             # Step 4: Translate notes
#             with st.spinner("Translating to Hindi..."):
#                 hindi_notes = translate_text(english_notes, "hi")

#             with st.spinner("Translating to Kannada..."):
#                 kannada_notes = translate_text(english_notes, "kn")

#             # Translation fallback
#             if not hindi_notes or "Error" in hindi_notes:
#                 hindi_notes = (
#                     "Translation failed. Showing English instead.\n\n"
#                     + english_notes
#                 )

#             if not kannada_notes or "Error" in kannada_notes:
#                 kannada_notes = (
#                     "Translation failed. Showing English instead.\n\n"
#                     + english_notes
#                 )

#             st.success("✅ Notes generated successfully!")

#             # Display notes in tabs
#             tab1, tab2, tab3 = st.tabs(
#                 ["English", "Hindi", "Kannada"]
#             )

#             # English tab
#             with tab1:

#                 st.text_area(
#                     "English Notes",
#                     english_notes,
#                     height=300
#                 )

#                 pdf_file = create_pdf(english_notes)

#                 st.download_button(
#                     label="📄 Download English PDF",
#                     data=pdf_file,
#                     file_name="notes_english.pdf",
#                     mime="application/pdf"
#                 )

#             # Hindi tab
#             with tab2:

#                 st.text_area(
#                     "Hindi Notes",
#                     hindi_notes,
#                     height=300
#                 )

#                 pdf_file = create_pdf(hindi_notes)

#                 st.download_button(
#                     label="📄 Download Hindi PDF",
#                     data=pdf_file,
#                     file_name="notes_hindi.pdf",
#                     mime="application/pdf"
#                 )

#             # Kannada tab
#             with tab3:

#                 st.text_area(
#                     "Kannada Notes",
#                     kannada_notes,
#                     height=300
#                 )

#                 pdf_file = create_pdf(kannada_notes)

#                 st.download_button(
#                     label="📄 Download Kannada PDF",
#                     data=pdf_file,
#                     file_name="notes_kannada.pdf",
#                     mime="application/pdf"
#                 )

#         except Exception as e:
#             st.error(f"❌ Error: {e}")


# #app.py
# import streamlit as st
# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# from utils.translator import translate_text 
# from utils.pdf_generator import create_pdf


# def format_notes(text):
#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     # Quick Summary
#     summary = ". ".join(sentences[:5])
#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     # Key Points
#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if len(sentence) > 20:
#             formatted += "• " + sentence + ".\n"

#     return formatted


# # UI setup
# st.set_page_config(page_title="NoteWise AI", layout="centered")

# st.title("🎥 YouTube Video Notes Generator")
# st.write("Generate smart notes from YouTube videos in multiple languages")

# # Input
# url = st.text_input("Paste YouTube URL here")

# # Button
# if st.button("Generate Notes"):

#     if url.strip() == "":
#         st.warning("Please enter a YouTube URL")
#     else:
#         try:
#             # Step 1: Download audio
#             with st.spinner("Downloading audio..."):
#                 audio_path = download_audio(url)

#             if not audio_path:
#                 st.error("❌ Failed to download audio. Try another video.")
#                 st.stop()

#             # Step 2: Transcribe
#             with st.spinner("Transcribing audio..."):
#                 transcript = transcribe_audio(audio_path)

#             if not transcript:
#                 st.error("❌ Transcription failed.")
#                 st.stop()

#             # Step 3: Generate notes
#             with st.spinner("Generating notes..."):
#                 english_notes = format_notes(transcript)

#             # Limit size for translation (VERY IMPORTANT)
#             english_notes = english_notes[:8000]

#             # Step 4: Translate
#             with st.spinner("Translating to Hindi..."):
#                 hindi_notes = translate_text(english_notes, "hi")

#             with st.spinner("Translating to Kannada..."):
#                 kannada_notes = translate_text(english_notes, "kn")

#             # Fallback if translation fails
#             if not hindi_notes or "Error" in hindi_notes:
#                 hindi_notes = "⚠️ Translation failed. Showing English instead.\n\n" + english_notes

#             if not kannada_notes or "Error" in kannada_notes:
#                 kannada_notes = "⚠️ Translation failed. Showing English instead.\n\n" + english_notes

#             st.success("✅ Notes generated successfully!")

#             # Tabs for output
#             tab1, tab2, tab3 = st.tabs(["English", "Hindi", "Kannada"])

#             with tab1:
#                 st.text_area("English Notes", english_notes, height=300)
#                 st.download_button("Download English", english_notes, file_name="notes_english.txt")

#             with tab2:
#                 st.text_area("Hindi Notes", hindi_notes, height=300)
#                 st.download_button("Download Hindi", hindi_notes, file_name="notes_hindi.txt")

#             with tab3:
#                 st.text_area("Kannada Notes", kannada_notes, height=300)
#                 st.download_button("Download Kannada", kannada_notes, file_name="notes_kannada.txt")

#         except Exception as e:
#             st.error(f"❌ Error: {e}")

# import streamlit as st
# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# from utils.translator import translate_text


# def format_notes(text):
#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     # Quick Summary
#     summary = ". ".join(sentences[:5])
#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     # Key Points
#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if len(sentence) > 20:
#             formatted += "• " + sentence + ".\n"

#     return formatted


# # UI setup
# st.set_page_config(page_title="NoteWise AI", layout="centered")

# st.title("🎥 AI Powered YouTube Video Notes Generator")
# st.write("Generate smart notes from YouTube videos in multiple languages")

# # Input
# url = st.text_input("Paste YouTube URL here")

# # Button
# if st.button("Generate Notes"):

#     if url.strip() == "":
#         st.warning("Please enter a YouTube URL")
#     else:
#         try:
#             # Step 1: Download audio
#             with st.spinner("Downloading audio..."):
#                 audio_path = download_audio(url)

#             # Step 2: Transcribe
#             with st.spinner("Transcribing audio..."):
#                 transcript = transcribe_audio(audio_path)

#             # Step 3: Generate notes
#             with st.spinner("Generating notes..."):
#                 english_notes = format_notes(transcript)

#             # Step 4: Translate
#             with st.spinner("Translating to Hindi..."):
#                 hindi_notes = translate_text(english_notes, "hi")

#             with st.spinner("Translating to Kannada..."):
#                 kannada_notes = translate_text(english_notes, "kn")

#             st.success("✅ Notes generated successfully!")

#             # Tabs for output
#             tab1, tab2, tab3 = st.tabs(["English", "Hindi", "Kannada"])

#             with tab1:
#                 st.text_area("English Notes", english_notes, height=300)
#                 st.download_button("Download English", english_notes, file_name="notes_english.txt")

#             with tab2:
#                 st.text_area("Hindi Notes", hindi_notes, height=300)
#                 st.download_button("Download Hindi", hindi_notes, file_name="notes_hindi.txt")

#             with tab3:
#                 st.text_area("Kannada Notes", kannada_notes, height=300)
#                 st.download_button("Download Kannada", kannada_notes, file_name="notes_kannada.txt")

#         except Exception as e:
#             st.error(f"❌ Error: {e}")

# import streamlit as st
# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# from utils.translator import translate_text
# from utils.ai_formatter import generate_smart_notes   # 🔥 NEW


# def format_notes(text):
#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     summary = ". ".join(sentences[:5])
#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if len(sentence) > 20:
#             formatted += "• " + sentence + "\n"

#     return formatted


# # UI
# st.set_page_config(page_title="NoteWise AI", layout="centered")

# st.title("🎥 NoteWise AI")
# st.write("Generate smart AI notes from YouTube videos in multiple languages")

# url = st.text_input("Paste YouTube URL here")

# if st.button("Generate Notes"):

#     if url.strip() == "":
#         st.warning("Please enter a YouTube URL")
#     else:
#         # Step 1: Download
#         with st.spinner("Downloading audio..."):
#             audio_path = download_audio(url)

#         if audio_path is None:
#             st.error("❌ Failed to download video. Try another video.")
#             st.stop()

#         # Step 2: Transcribe
#         with st.spinner("Transcribing audio..."):
#             transcript = transcribe_audio(audio_path)

#         # Step 3: AI Smart Notes 🔥
#         with st.spinner("Generating AI smart notes... (first time may take time)"):
#             raw_notes = generate_smart_notes(transcript)

#         # Step 4: Format
#         with st.spinner("Formatting notes..."):
#             english_notes = format_notes(raw_notes)

#         # Step 5: Translate
#         with st.spinner("Translating to Hindi..."):
#             hindi_notes = translate_text(english_notes, "hi")

#         with st.spinner("Translating to Kannada..."):
#             kannada_notes = translate_text(english_notes, "kn")

#         st.success("✅ Notes generated successfully!")

#         # Tabs
#         tab1, tab2, tab3 = st.tabs(["English", "Hindi", "Kannada"])

#         with tab1:
#             st.text_area("English Notes", english_notes, height=300)
#             st.download_button("Download English", english_notes, file_name="notes_english.txt")

#         with tab2:
#             st.text_area("Hindi Notes", hindi_notes, height=300)
#             st.download_button("Download Hindi", hindi_notes, file_name="notes_hindi.txt")

#         with tab3:
#             st.text_area("Kannada Notes", kannada_notes, height=300)
#             st.download_button("Download Kannada", kannada_notes, file_name="notes_kannada.txt")

# import streamlit as st
# from utils.downloader import download_audio
# from utils.transcriber import transcribe_audio
# from utils.translator import translate_text


# def format_notes(text):
#     sentences = text.split(". ")

#     formatted = "📘 SMART NOTES\n"
#     formatted += "=" * 40 + "\n\n"

#     summary = ". ".join(sentences[:5])
#     formatted += "🔹 Quick Summary:\n"
#     formatted += summary.strip() + ".\n\n"

#     formatted += "🔹 Key Points:\n\n"

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if len(sentence) > 20:
#             formatted += "• " + sentence + ".\n"

#     return formatted


# # UI
# st.set_page_config(page_title="NoteWise AI", layout="centered")

# st.title("🎥 NoteWise AI")
# st.write("Generate smart notes from YouTube videos in multiple languages")

# url = st.text_input("Paste YouTube URL here")

# if st.button("Generate Notes"):

#     if url.strip() == "":
#         st.warning("Please enter a YouTube URL")
#     else:
#         with st.spinner("Downloading audio..."):
#             audio_path = download_audio(url)

#         with st.spinner("Transcribing audio..."):
#             transcript = transcribe_audio(audio_path)

#         with st.spinner("Generating English notes..."):
#             english_notes = format_notes(transcript)

#         with st.spinner("Translating to Hindi..."):
#             hindi_notes = translate_text(english_notes, "hi")

#         with st.spinner("Translating to Kannada..."):
#             kannada_notes = translate_text(english_notes, "kn")

#         st.success("✅ Notes generated successfully!")

#         # Tabs for languages
#         tab1, tab2, tab3 = st.tabs(["English", "Hindi", "Kannada"])

#         with tab1:
#             st.text_area("English Notes", english_notes, height=300)
#             st.download_button("Download English", english_notes, file_name="notes_english.txt")

#         with tab2:
#             st.text_area("Hindi Notes", hindi_notes, height=300)
#             st.download_button("Download Hindi", hindi_notes, file_name="notes_hindi.txt")

#         with tab3:
#             st.text_area("Kannada Notes", kannada_notes, height=300)
#             st.download_button("Download Kannada", kannada_notes, file_name="notes_kannada.txt")