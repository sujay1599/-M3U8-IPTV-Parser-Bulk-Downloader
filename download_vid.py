import pandas as pd
import requests
import os
import re
import time
from tqdm import tqdm

def sanitize_filename(name):
    """Remove illegal characters from filenames (Windows-safe)"""
    # Replace characters that are illegal in Windows filenames with an underscore
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def download_with_progress(url, output_path, max_retries=5, retry_delay=5):
    """
    Download a file with a progress bar, speed tracking, resume capability, and retries.

    Args:
        url (str): The URL of the file to download.
        output_path (str): The local path where the file will be saved.
        max_retries (int): Maximum number of times to retry a failed download.
        retry_delay (int): Delay in seconds between retries.
    """
    retries = 0
    # Define a default User-Agent to mimic a web browser
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }

    while retries < max_retries:
        try:
            # Initialize headers for the current request, starting with default_headers
            request_headers = default_headers.copy()
            file_mode = 'wb'  # Default to write binary (new file)
            current_size = 0

            if os.path.exists(output_path):
                current_size = os.path.getsize(output_path)
                # If the file exists and has some content, try to resume
                if current_size > 0:
                    file_mode = 'ab'  # Append binary
                    # Add the Range header to the existing request_headers
                    request_headers['Range'] = f'bytes={current_size}-'
                    print(f"🔄 Resuming download for {os.path.basename(output_path)} from {current_size} bytes...")

            # Make the GET request with streaming and specified headers
            with requests.get(url, stream=True, timeout=60, headers=request_headers) as r:
                # This line checks for successful HTTP status codes (2xx).
                # If the response is not 2xx, it raises an HTTPError.
                r.raise_for_status()

                # Get total size, considering if it's a resumed download
                total_size = int(r.headers.get('content-length', 0))
                if total_size == 0: # If content-length is not provided or is 0, assume full download size
                    # This might happen if the server doesn't support Range requests or for small files
                    if 'Content-Range' in r.headers:
                        content_range = r.headers['Content-Range']
                        match = re.search(r'/(\d+)$', content_range)
                        if match:
                            total_size = int(match.group(1))
                    elif current_size > 0: # If it's a resume but no content-range, assume full size is current_size + new_content_length
                        total_size += current_size
                    else: # Fallback if no size info, set to a large number to avoid division by zero in tqdm
                        total_size = None # tqdm handles None total gracefully

                # If resuming, the total_size from headers is only the *remaining* size.
                # We need the full file size for the progress bar.
                if 'Content-Range' in r.headers and current_size > 0:
                    # Example: Content-Range: bytes 206848-1234567/1234568
                    full_total_size_match = re.search(r'/(\d+)$', r.headers['Content-Range'])
                    if full_total_size_match:
                        total_size = int(full_total_size_match.group(1))
                    else:
                        total_size = current_size + total_size # Fallback if Content-Range is weird

                # If the current_size is already equal to or greater than the total_size, it's already downloaded
                if total_size is not None and current_size >= total_size:
                    print(f"✅ Already downloaded: {os.path.basename(output_path)}")
                    return

                block_size = 8012  # Changed chunk size to 8KB for downloading
                wrote = 0

                start_time = time.time()
                with open(output_path, file_mode) as f, tqdm(
                    total=total_size,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024,
                    desc=os.path.basename(output_path),
                    initial=current_size, # Set initial progress for resume
                    ascii=True,
                    dynamic_ncols=True
                ) as bar:
                    for chunk in r.iter_content(chunk_size=block_size):
                        if chunk:
                            f.write(chunk)
                            wrote += len(chunk)
                            bar.update(len(chunk))

                # After the download loop, verify the total downloaded size
                final_downloaded_size = current_size + wrote
                if total_size is not None and final_downloaded_size < total_size:
                    raise requests.exceptions.RequestException(
                        f"Content length mismatch: Expected {total_size} bytes, got {final_downloaded_size} bytes."
                    )

                end_time = time.time()
                elapsed = end_time - start_time
                # Calculate speed based on bytes written in this session
                speed = (wrote / 1024 / 1024) / elapsed if elapsed > 0 else 0
                print(f"✅ Done! Speed: {speed:.2f} MB/s")
                return # Exit function on successful download

        except requests.exceptions.RequestException as e:
            retries += 1
            print(f"❌ Network error or request issue for {os.path.basename(output_path)}: {e}")
            if retries < max_retries:
                print(f"Retrying in {retry_delay} seconds... ({retries}/{max_retries})")
                time.sleep(retry_delay)
            else:
                print(f"🛑 Max retries reached for {os.path.basename(output_path)}. Skipping.")
                return
        except Exception as e:
            # Catch any other unexpected errors
            print(f"❌ An unexpected error occurred for {os.path.basename(output_path)}: {e}")
            return # Do not retry for unexpected errors, as they might be persistent

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
