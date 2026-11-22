#downloader.py
import yt_dlp
import os
import uuid

def download_audio(url):
    try:
        os.makedirs("temp", exist_ok=True)

        unique_id = str(uuid.uuid4())
        output_path = f"temp/{unique_id}.%(ext)s"

        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio/best',  # 🔥 stable fallback
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'quiet': True,
            'nocache': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        final_path = f"temp/{unique_id}.mp3"

        return final_path

    except Exception as e:
        print("Download Error:", e)
        return None

# import yt_dlp
# import os
# import uuid

# def download_audio(url):

#     os.makedirs("temp", exist_ok=True)

#     unique_id = str(uuid.uuid4())  # 🔥 unique name

#     output_path = f"temp/{unique_id}.%(ext)s"

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': output_path,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#         }],
#         'quiet': True,
#         'nocache': True
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.extract_info(url, download=True)

#     final_path = f"temp/{unique_id}.mp3"

#     return final_path

# import yt_dlp
# import os
# import glob

# def download_audio(url):

#     os.makedirs("temp", exist_ok=True)

#     # 🔥 CLEAR OLD FILES
#     old_files = glob.glob("temp/*.mp3")
#     for file in old_files:
#         os.remove(file)

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': 'temp/%(id)s.%(ext)s',   # use video id (IMPORTANT)
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#         }],
#         'quiet': False,
#         'nocache': True,          # 🔥 disable cache
#         'overwrites': True        # 🔥 overwrite old files
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)

#         video_id = info['id']
#         filename = f"temp/{video_id}.mp3"

#     print(f"Audio downloaded at: {filename}")

#     return filename

# import yt_dlp
# import os
# import glob

# def download_audio(url):

#     os.makedirs("temp", exist_ok=True)

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': 'temp/%(title)s.%(ext)s',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#         }],
#         'quiet': True
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.extract_info(url, download=True)

#     # get latest mp3 file from temp folder
#     files = glob.glob("temp/*.mp3")

#     if not files:
#         raise FileNotFoundError("No audio file found in temp folder")

#     latest_file = max(files, key=os.path.getctime)

#     print(f"Audio downloaded at: {latest_file}")

#     return latest_file

# import yt_dlp
# import uuid
# import os

# def download_audio(url):

#     os.makedirs("temp", exist_ok=True)

#     filename = f"temp/{uuid.uuid4()}.mp3"

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': filename,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#         }],
#         'quiet': True
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

#     return filename

# import yt_dlp
# import os
# import uuid

# TEMP_DIR = "temp"

# def download_audio(youtube_url):
#     """
#     Downloads audio from YouTube and saves it as mp3 in temp folder.
#     Returns the file path of downloaded audio.
#     """

#     # Ensure temp folder exists
#     if not os.path.exists(TEMP_DIR):
#         os.makedirs(TEMP_DIR)

#     # Generate unique filename
#     unique_id = str(uuid.uuid4())
#     output_path = os.path.join(TEMP_DIR, f"{unique_id}.%(ext)s")

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': output_path,
#         'quiet': True,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([youtube_url])

#     # Final file path after conversion
#     final_file = os.path.join(TEMP_DIR, f"{unique_id}.mp3")

#     return final_file