from pathlib import Path
import yt_dlp
import csv

def download_video(url):
    Path("videos").mkdir(exist_ok=True)

    ydl_options = {
    "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

def read_video_urls(csv_path):
    url_list = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            url_list.append(row["url"]) 
    return url_list

def get_video_metadata(url):
    ydl_options = {
            "quiet": True,
            "skip_download": True,
            }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(url, download=False)
        print("Title:", info.get("title"))
        print("Duration:", info.get("duration"))
        print("Uploader:", info.get("uploader"))
        print("Views:", info.get("view_count"))
        print("Extension:", info.get("ext"))
        print("URL:", url)
        return {
                "title": info.get("title"),
                "duration": info.get("duration"),
                "uploader": info.get("uploader"),
                "view_count": info.get("view_count"),
                "ext": info.get("ext"),
                "url": url
                }
