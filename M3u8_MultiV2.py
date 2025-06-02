import re
import pandas as pd
import os

# Paste your M3U8 content here
full_input_text_extended = """

#EXTINF:-1 tvg-logo="http://img-cdn.curl.pk/chimg/10308378765022.jpg" group-title="xxx" tvg-id="" tvg-name="", Super Star_247
http://sptvcs.com:8880/movie/49800099/37071227/562210.mp4

#EXTINF:-1 tvg-logo="http://img-cdn.curl.pk/chimg/10633362957776.jpg" group-title="xxx" tvg-id="" tvg-name="", Super Star_244
http://sptvcs.com:8880/movie/49800099/37071227/562207.mp4

#EXTINF:-1 tvg-logo="http://img-cdn.curl.pk/chimg/10679490104413.jpg" group-title="xxx" tvg-id="" tvg-name="", Super Star_246
http://sptvcs.com:8880/movie/49800099/37071227/562209.mp4


"""

# Split the input text into individual lines
lines = full_input_text_extended.strip().splitlines()

# Initialize an empty list to store the parsed data
result = []
# Initialize a set to keep track of seen entries (full_filename, link_line) to avoid duplicates
seen_entries = set()

# Iterate through the lines, processing two lines at a time (EXTINF and URL)
for i in range(0, len(lines), 2):
    # Ensure there are at least two lines remaining to process a complete entry
    if i + 1 < len(lines):
        title_line = lines[i]
        link_line = lines[i + 1].strip() # Get the URL line and remove leading/trailing whitespace

        # Extract the actual title which comes after the last comma on the EXTINF line
        title_match = re.search(r',([^,]+)$', title_line)
        if title_match:
            base_name = title_match.group(1).strip() # Extract the title value
            ext = os.path.splitext(link_line)[1] # Extract the file extension from the URL
            full_filename = base_name + ext # Combine base name and extension for full filename

            # Create a unique key for the current entry to check for duplicates
            entry_key = (full_filename, link_line)

            # Check if this entry has already been seen
            if entry_key not in seen_entries:
                seen_entries.add(entry_key) # Add the new unique entry to the set

                # Attempt to extract season (Sxx) and episode (Exx) numbers from the base_name
                # using regex. The \d{1,2} matches one or two digits.
                season_match = re.search(r'[Ss](\d{1,2})', base_name)
                episode_match = re.search(r'[Ee](\d{1,2})', base_name)

                # Format season and episode numbers with leading zeros if found, otherwise leave empty
                season = f"S{int(season_match.group(1)):02}" if season_match else ""
                episode = f"E{int(episode_match.group(1)):02}" if episode_match else ""

                # Append the extracted data as a tuple to the result list
                result.append((base_name, full_filename, link_line, season, episode))
        else:
            # If no title found after comma, skip this entry to avoid errors
            continue

# Create a Pandas DataFrame from the collected results
df = pd.DataFrame(result, columns=[
    "File Name",
    "Full File Name",
    "Download Link",
    "Season",
    "Episode"
])

# Save the DataFrame to a CSV file
# index=False prevents Pandas from writing the DataFrame index as a column in the CSV
df.to_csv("output_with_season_episode.csv", index=False)

# Print a confirmation message
print("✅ Saved as output_with_season_episode.csv")
