import re
import pandas as pd
import os

# Paste your M3U8 content here
full_input_text_extended = """

#EXTINF:-1 tvg-id="" tvg-name="The Walking Dead: Daryl Dixon S01 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/3oebI0Euvz8C4IPMAu346RcV2Gh.jpg" group-title="English",The Walking Dead: Daryl Dixon S01 E01
http://wanicelife.com:8880/series/DAALM2983/8GFr6cbUd7/82794.mkv
#EXTINF:-1 tvg-id="" tvg-name="The Walking Dead: Daryl Dixon S01 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/gCTcN8Wl9Pn3BuU6sJX2fqdxomb.jpg" group-title="English",The Walking Dead: Daryl Dixon S01 E02
http://wanicelife.com:8880/series/DAALM2983/8GFr6cbUd7/82795.mkv
#EXTINF:-1 tvg-id="" tvg-name="The Walking Dead: Daryl Dixon S01 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/wSdflUF8nlcgDb6WFXRd1R7tPTC.jpg" group-title="English",The Walking Dead: Daryl Dixon S01 E03
http://wanicelife.com:8880/series/DAALM2983/8GFr6cbUd7/82796.mkv
#EXTINF:-1 tvg-id="" tvg-name="The Walking Dead: Daryl Dixon S01 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/l7Xj2excN8Ffx31qt3KTa68KKot.jpg" group-title="English",The Walking Dead: Daryl Dixon S01 E04


"""

lines = full_input_text_extended.strip().splitlines()

result = []
for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        title_line = lines[i]
        link_line = lines[i + 1].strip()

        match = re.search(r'tvg-name="([^"]+)"', title_line)
        if match:
            base_name = match.group(1).strip()
            ext = os.path.splitext(link_line)[1]
            full_filename = base_name + ext

            # Extract Sxx and Exx if available
            season_match = re.search(r'[Ss](\d{1,2})', base_name)
            episode_match = re.search(r'[Ee](\d{1,2})', base_name)

            season = f"S{int(season_match.group(1)):02}" if season_match else ""
            episode = f"E{int(episode_match.group(1)):02}" if episode_match else ""

            result.append((base_name, full_filename, link_line, season, episode))

# Create DataFrame
df = pd.DataFrame(result, columns=[
    "File Name", 
    "Full File Name", 
    "Download Link", 
    "Season", 
    "Episode"
])

# Save to CSV
df.to_csv("output_with_season_episode.csv", index=False)
print("✅ Saved as output_with_season_episode.csv")
