import sys
from pytube import Playlist, YouTube

# Function to download and choose the resolution of a single video
def download_video(video, resolution="audio", path="."):
    try:
        if resolution == "audio":
            video_stream = video.streams.filter(only_audio=True).first()
        elif resolution == "low":
            video_stream = video.streams.filter(res="360p").first()
        elif resolution == "high":
            video_stream = video.streams.filter(res="720p").first()
        else:
            print(f"Invalid resolution option: {resolution}")
            return

        if video_stream:
            print(f'\nChannel Name: {video.author}')
            print(f"Video Title: {video.title}")
            print(f'Number of Views: {video.views}')
            print(f'Video Length: {round((video.length)/60, 3)} Minutes.')
            print(f'Published Date: {video.publish_date}. \n')

            print(f"Downloading: {video.title}")
            video_stream.download(output_path=path)
            print(f"{video.title} downloaded successfully.")

        else:
            print(f"No suitable stream found for {video.title}")

    except Exception as e:
        print(f"Error downloading {video.title}: {e}")

# Function to download a playlist using pytube
def download_playlist(playlist_url, resolution="audio", path="."):
    try:
        playlist = Playlist(playlist_url)
        print(f"Downloading playlist: {playlist.title}")

        for video_url in playlist.video_urls:
            video = YouTube(video_url)
            download_video(video, resolution, path)
            print("")

        print("Playlist download completed.")

    except Exception as e:
        print(f"Error downloading playlist {playlist_url}: {e}")


try:
    playlist_url = input("Enter the YouTube playlist URL: ")
    path = input('Enter Your Download path: ')
    resolution_choice = input("Choose resolution (high/low/audio): ").lower()

    if resolution_choice not in ["high", "low", "audio"]:
        print("Invalid resolution choice.")
        sys.exit()

    download_playlist(playlist_url, resolution=resolution_choice, path=path)

except KeyboardInterrupt:
    print("\nDownload interrupted by the user.")
    sys.exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
