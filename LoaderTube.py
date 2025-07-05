from colorama import Fore
import os, sys, yt_dlp, time, subprocess,platform

def set_utf8_encoding():
    system_name = platform.system().lower()
    if system_name == "windows":
        os.system("chcp 65001 >nul")
    elif system_name in ["linux", "darwin"]:
        os.environ["LANG"] = "en_US.UTF-8"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def clear_screen():
    system_name = platform.system().lower()
    os.system("cls" if system_name == "windows" else "clear")
    print(f"{Fore.BLUE}{"-"*30}")
    print(f"{Fore.GREEN}{" "*6}Free Palestine") # 🇵🇸
    print(f"{Fore.RED}{" "*2}Dev By ❤️ Mahamed Emad")
    print(f"{Fore.BLUE}{"-"*30}\n")

def select_videos(_Range, Len):
    Range = set()
    _Range = _Range.replace(" ", "").split(",")

    for part in _Range:
        if "-" in part:
            for i in range(int(part[:part.find("-")]), int(part[part.find("-")+ 1:])+ 1):
                if i <= Len: Range.add(i)
        else:
            if int(part) <= Len: Range.add(int(part))

    Range = sorted(list(Range))
    return Range

def download_video():

    clear_screen()
    url = input(f"{Fore.YELLOW}Enter URL: ").strip()
    resolution = input("Enter Quality [mp3, 1080p] \"720p default\": ").strip().lower().replace(" ", "")
    resolution = resolution.replace("p" if "m" not in resolution else resolution, "mp3")
    resolution = resolution if resolution in \
        ["144", "240", "360", "480", "720", "1080", "1440", "2160", "mp3"] else "720"

    save_path = os.path.join(os.getcwd(), "Downloads")
    os.makedirs(save_path, exist_ok=True)

    if resolution == "mp3":
        video_downloader_option = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'noplaylist': False,
        'ignoreerrors': True,
        'verbose': False,
        'external_downloader': 'aria2c',
        'external_downloader_args': ['--min-split-size=1M', '--max-connection-per-server=16', '--max-concurrent-downloads=16'],
        'concurrent_fragment_downloads': 14,
        'throttledratelimit': None,
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'}]}

    else:
        video_downloader_option = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': f'bestvideo[height<={resolution}]+bestaudio/best',
            'merge_output_format': 'mp4',
            'noplaylist': False,
            'ignoreerrors': True,
            'verbose': False,
            'external_downloader': 'aria2c',
            'external_downloader_args': ['--min-split-size=1M', '--max-connection-per-server=16', '--max-concurrent-downloads=16'],
            'concurrent_fragment_downloads': 14,
            'throttledratelimit': None,
            'ffmpeg_location': resource_path('ffmpeg.exe')}
    clear_screen()

    try:
        with yt_dlp.YoutubeDL(video_downloader_option) as ydl:
            resolution_downloaded = None
 
            if "playlist?" not in url:

                if "list=" in url:
                    url = url[:url.find("&list=")]
                elif "?list=" in url:
                    url = url[:url.find("?list=")]
                ydl.download([url])

                info = ydl.extract_info(url, download=False)
                if resolution != "mp3" and 'height' in info and info['height'] is not None:
                    resolution_downloaded = info['height']
                elif resolution != "mp3" and 'requested_downloads' in info and info['requested_downloads']:
                    info = ydl.extract_info(url, download=False)
                    resolution_downloaded = info['requested_downloads'][0].get('height')

            else:
                info = ydl.extract_info(url, download=False)
                clear_screen()
                parts = input("Enter The Index Videos You Want Download `All Default` (e.g. 1,3,5-7): ")
                Range = select_videos(parts, len(info['entries'])) if parts else range(1, len(info['entries']) + 1)
                clear_screen()

                for i, index in enumerate(Range, 1):
                    video = info['entries'][index - 1]

                    if video:
                        video_url = video.get('webpage_url')
                        if resolution != "mp3" and not resolution_downloaded:
                            video_info = ydl.extract_info(video_url, download=True)
                            if 'height' in video_info and video_info['height']:
                                resolution_downloaded = video_info['height']
                            elif 'requested_downloads' in video_info and video_info['requested_downloads']:
                                resolution_downloaded = video_info['requested_downloads'][0].get('height')

                        ydl.download([video_url])
                        print(f"{Fore.GREEN}\n\n\t ✅ {i}/{len(Range)} Downloaded ✅{Fore.RESET}\n\n")

            clear_screen()
            print(f"{Fore.YELLOW}=>> URL: {url}\n=>> Quality: {f"{resolution_downloaded}p" if resolution != "mp3" else resolution}")

            print("\n" if "playlist?" not in url else f"=>> Range: {
                f"{len(info['entries'])} videos \"All Playlist\"" \
                if len(info['entries']) == len(list(Range)) else list(Range)}\n")

            for i in range(1, 5): print(f"   {Fore.GREEN}- Done {int((i/4)*100)}%✅" if i < 4 else f" ✅ Done {int((i/4)*100)}% ✅"); time.sleep(1)
            print(f"{Fore.CYAN}\n >> ✅ Downloaded Successfully ✅ <<\n\n")

    except Exception as e:
        print(f"{Fore.RED}\n\n==> ❌ Error: {e}\n\n")

def open_download_window():
    system_name = platform.system().lower()
    downloads_path = os.path.join(os.getcwd(), "Downloads")

    if system_name == "windows":
        subprocess.Popen(f'explorer "{downloads_path}"')
    elif system_name == "darwin":
        subprocess.Popen(["open", downloads_path])
    else:
        subprocess.Popen(["xdg-open", downloads_path])

def LoaderTube():
    set_utf8_encoding()
    download_video()
    open_download_window()

while True:
    LoaderTube()
    if input(f"{Fore.BLUE}To Download Other Videos Enter `Y`: ").lower().strip() == "y":
        time.sleep(0.5); continue
    else:
        print(f"{Fore.CYAN}\nExiting Program... 👋")
        time.sleep(2.5)
        sys.exit()


# أضيف أسمي كالناشر
# pyinstaller --onefile --name "LoaderTube" --icon=icon.ico --add-binary "ffmpeg.exe;." --add-binary "ffprobe.exe;." LoaderTube.py