Here is the `README.md` content **embedded directly into your codebase**, using a multi-line comment at the top of `M3u8_MultiV2.py`:

---

### ✅ Updated `M3u8_MultiV2.py` (with README embedded)

Paste this at the top of your script:

````python
"""
# 📺 M3U8 IPTV Parser & Bulk Downloader

Parse `.m3u8` IPTV playlists and auto-download video streams with smart file naming, including optional Season/Episode tagging and safe filename sanitization. Ideal for organizing IPTV shows and direct `.mp4`/`.mkv` streams.

---

## 🔧 Features

- ✅ Parses `.m3u8` or `.m3u`-formatted text
- ✅ Extracts:
  - File name
  - Extension
  - Direct download link
  - Season & Episode (e.g., `S01E04`) if present
- ✅ Prevents duplicate entries
- ✅ Exports to structured `CSV`
- ✅ Resumable downloads with retry support
- ✅ Real-time progress bar with download speed tracking
- ✅ OS-safe filename generation

---

## 📂 Included Files

| File               | Purpose                                                         |
|--------------------|-----------------------------------------------------------------|
| `M3u8_MultiV2.py`  | Parses raw M3U8-formatted text and generates a CSV              |
| `download2.py`     | Downloads media files using `requests` and `tqdm` with retries  |

---

## 🚀 How to Use

### 1. Parse M3U8 Input

1. Open `M3u8_MultiV2.py`
2. Paste your M3U8 content into the `full_input_text_extended` string
3. Run:

```bash
python M3u8_MultiV2.py
````

✅ Output: `output_with_season_episode.csv`

---

### 2. Download Videos

Run the downloader:

```bash
python download2.py
```

📦 When prompted:

```
📁 Enter folder path to save videos (press Enter for default 'downloads'):
```

---

## 🧪 Sample Output

| File Name               | Full File Name              | Download Link                                  | Season | Episode |
| ----------------------- | --------------------------- | ---------------------------------------------- | ------ | ------- |
| Super Star\_244         | Super Star\_244.mp4         | [http://.../562207.mp4](http://.../562207.mp4) |        |         |
| The Walking Dead S01E01 | The Walking Dead S01E01.mkv | [http://.../82794.mkv](http://.../82794.mkv)   | S01    | E01     |

---

## 📥 Output Example

⬇️ Starting: Super Star\_244.mp4
Super Star\_244.mp4: 85%|████████▌ | 85.0M/100M \[00:05<00:01, 12.1MB/s]
✅ Done! Speed: 11.91 MB/s

---

## 💡 Tips

* URLs must be direct links (e.g., `.mp4`, `.mkv`)
* Use a VPN if download links are region-locked
* You can edit `chunk_size` in `download2.py` for performance tuning
* File names are auto-sanitized for Windows/macOS/Linux compatibility

---

## 🧱 Dependencies

Install required Python packages:

```bash
pip install pandas tqdm requests
```

---

## 📌 To-Do / Future Features

* [ ] Input support for `.m3u` file upload
* [ ] Auto-tagging based on custom rules (e.g., `Super Star_244` → `S01E244`)
* [ ] Shuffle/random download order
* [ ] Parallel/multi-threaded downloads
* [ ] GUI front-end with drag-and-drop support

---

## ⚠️ Disclaimer

This tool is intended for personal and educational use only. Make sure you have permission to download the media from the source links provided.

---

"""

```

USE A VPN
USE A VPN
USE A VPN
USE A VPN
USE A VPN
USE A VPN

```
