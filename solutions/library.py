from pathlib import Path
import yt_dlp

def download_video(url):
    Path("videos").mkdir(exist_ok=True)

    ydl_options = {
    "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])
