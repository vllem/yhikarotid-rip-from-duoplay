import subprocess

def download_season(season_file, season_name, episode_prefix):
    with open(season_file, 'r') as file:
        episode_number = 1
        for line in file:
            url = line.strip()
            if url:
                filename = f"{season_name} {episode_prefix} {episode_number}.mp4"
                subprocess.run(["yt-dlp", "-o", filename, "-f", "0", url])
                episode_number += 1

seasons = ["Hooaeg 1", "Hooaeg 2", "Hooaeg 3", "Hooaeg 4"]
episode_prefix = "Episood"

for season in seasons:
    download_season(f"{season}.txt", season, episode_prefix)

