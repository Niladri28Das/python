import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading...")
            ydl.download([url])
            print("Done! ✅")
    except Exception as e:
        print("Error ❌")
        print(e)


if __name__ == "__main__":
    link = input("Enter YouTube video URL: ").strip()
    download_video(link)
