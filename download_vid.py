import pandas as pd
import requests
import os
import re
import time
from tqdm import tqdm

def sanitize_filename(name):
    """Remove illegal characters from filenames (Windows-safe)"""
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def download_with_progress(url, output_path):
    """Download a file with progress bar and speed tracking"""
    try:
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            block_size = 8192  # 8KB
            wrote = 0

            start_time = time.time()
            with open(output_path, 'wb') as f, tqdm(
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                desc=os.path.basename(output_path),
                initial=0,
                ascii=True,
                dynamic_ncols=True
            ) as bar:
                for chunk in r.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        wrote += len(chunk)
                        bar.update(len(chunk))

            end_time = time.time()
            elapsed = end_time - start_time
            speed = (wrote / 1024 / 1024) / elapsed if elapsed > 0 else 0
            print(f"✅ Done! Speed: {speed:.2f} MB/s")

    except Exception as e:
        print(f"❌ Failed: {os.path.basename(output_path)} — {e}")

def main():
    save_dir = input("📁 Enter folder path to save videos (press Enter for default 'downloads'): ").strip()
    if not save_dir:
        save_dir = "downloads"
    os.makedirs(save_dir, exist_ok=True)

    csv_path = "output_with_season_episode.csv"
    if not os.path.exists(csv_path):
        print(f"❌ CSV file not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    for index, row in df.iterrows():
        full_filename = sanitize_filename(row["Full File Name"])
        url = row["Download Link"]
        save_path = os.path.join(save_dir, full_filename)

        if not url or pd.isna(url):
            print(f"⚠️ Skipping (no URL): {full_filename}")
            continue

        print(f"\n⬇️ Starting: {full_filename}")
        download_with_progress(url, save_path)

if __name__ == "__main__":
    main()
