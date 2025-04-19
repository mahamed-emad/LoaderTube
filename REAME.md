# 🚀 LoaderTube

**LoaderTube** is a powerful, fast, and flexible YouTube downloader built with Python.  
It lets you download single videos or full playlists in various resolutions or convert them directly into MP3 — all from a simple terminal interface!

---

## 🎯 Features

- 🔹 **Download YouTube videos in high quality** (144p → 2160p)
- 🔹 **Convert videos to MP3** with automatic audio extraction
- 🔹 **Support for full Playlists**, with option to select specific videos
- 🔹 **Multi-threaded downloading** via `aria2c` for maximum speed
- 🔹 **High-quality audio/video merging** via `ffmpeg`
- 🔹 **Simple CLI interface** with colored prompts

---

## 🛠️ Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [yt_dlp](https://github.com/yt-dlp/yt-dlp)
- [aria2c](https://aria2.github.io/)
- [ffmpeg](https://ffmpeg.org/)

### Install dependencies:
```bash
pip install yt_dlp colorama


تمام، جهزت لك ملف `README.md` احترافي تقدر تحطه مباشرة في مشروعك على GitHub أو أي منصة نشر كـ open source.

------------------------------------------------------------

## ⚙️ How to Use

1. Clone the repo:
```bash
git clone https://github.com/mahamed-emad/LoaderTube.git
cd LoaderTube
```

2. Run the script:
```bash
python loadertube.py
```

3. Paste a video or playlist URL when prompted.

4. Choose download quality:
   - Enter `mp3` for audio
   - Or a resolution like `1080p`, `720p`, etc.

5. For playlists, you can:
   - Download **all videos** (default)
   - Or select specific ones like: `1,3,5-8`

6. Files are saved automatically to a `Downloads` folder.

---


## 📌 To-Do (Future Plans)

- [ ] GUI version using Tkinter or PyQt
- [ ] More format support (m4a, wav...)
- [ ] Dark mode CLI
- [ ] Download subtitles or thumbnails
- [ ] URL validation and better error handling

---

## 👨‍💻 Author

**Mahamed Emad**  
💬 If you find it useful, give it a ⭐ and share it!

Connect:
- [LinkedIn](https://linkedin.com/in/mahamed-emad)
- [Email](mahamed.emad.barakat@gmail.com)

---

## 🛡 License

This project is open-source
```
