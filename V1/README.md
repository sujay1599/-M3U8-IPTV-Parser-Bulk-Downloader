# 📺 M3U8 IPTV Parser & Bulk Downloader

**Parse `.m3u8` IPTV files and auto-download media** with properly named filenames including Season & Episode tagging. Perfect for organizing shows from IPTV sources or free streaming lists.

---

## 🔧 Features

- Extracts:
  - ✅ File name (no extension)
  - ✅ Full file name with original extension
  - ✅ Direct download link
  - ✅ Season & Episode (like `S01E04`)
- Generates a clean CSV file
- Optional folder input for saving downloads
- Streamed downloading with live progress bar and download speed
- Safe filename sanitization (Windows/macOS/Linux compatible)

---

## 📂 Files Included

| File Name           | Description                                           |
|---------------------|-------------------------------------------------------|
| `M3u8_MultiV2.py`   | Parses `.m3u8` text and outputs a structured CSV file |
| `download_vid.py`   | Downloads all media files from the CSV using `requests` with a tqdm progress bar |

---

## 🚀 How to Use

### 1. Parse the M3U8 File

Open and edit `M3u8_MultiV2.py`, paste your M3U8 content into the `full_input_text_extended` string, and run:

```bash
python M3u8_MultiV2.py
```

This creates:
```
output_with_season_episode.csv
```

### 2. Download the Videos

Run the downloader and specify where you want files saved:

```bash
python download_vid.py
```

It will ask:

```
📁 Enter folder path to save videos (press Enter for default 'downloads'):
```

- Hit Enter to use the default `downloads/` folder
- Or type a full path like `D:\IPTV_Shows` or `./Media`

---

## 🧪 Example

Sample entry in `output_with_season_episode.csv`:

| File Name                           | Full File Name                         | Download Link                             | Season | Episode |
|------------------------------------|----------------------------------------|--------------------------------------------|--------|---------|
| The Walking Dead: Daryl Dixon S01 E01 | The Walking Dead: Daryl Dixon S01 E01.mkv | http://fake-streaming.net/.../82794.mkv | S01    | E01     |

---

## 🔽 Example Output

```plaintext
⬇️ Starting: The Walking Dead: Daryl Dixon S01 E01.mkv
The Walking Dead: Daryl Dixon S01 E01.mkv: 85%|████████▌ | 85.0M/100M [00:05<00:01, 12.1MB/s]
✅ Done! Speed: 11.91 MB/s
```

---

## 📦 Requirements

Install Python dependencies:

```bash
pip install pandas tqdm requests
```

---

## 💡 Tips

- You can increase download speed by using a larger `chunk_size` in `download_with_progress()`
- All filenames are sanitized to prevent OS conflicts
- URLs must be **direct media links** (e.g., `.mp4`, `.mkv`, `.avi`)

---

## 📌 To-Do / Future Features

- [ ] Auto-detect `group-title` as categories
- [ ] Support for `.m3u` file input (instead of pasting text)
- [ ] Parallel downloading (threaded/async)
- [ ] GUI interface with drag-and-drop support