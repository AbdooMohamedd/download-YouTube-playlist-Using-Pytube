# download-YouTube-playlist-Using-Pytube
# YouTube Playlist Downloader

YouTube Playlist Downloader is a Python script that allows you to download videos from a YouTube playlist in various resolutions, including audio-only.

## Features

- Download entire YouTube playlists
- Choose video resolution: high (720p), low (360p), or audio-only
- Detailed video information display before download

## Prerequisites

- Python 3.x
- `pytube` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AbdooMohamedd/download-YouTube-playlist-Using-Pytube.git
    cd download-YouTube-playlist-Using-Pytube
    ```

2. Install the required Python libraries:

    ```bash
    pip install pytube
    ```

## Usage

1. Run the script:

    ```bash
    python Download youtube playlist .py
    ```

2. Enter the YouTube playlist URL when prompted:

    ```
    Enter the YouTube playlist URL: <your-playlist-url>
    ```

3. Enter the download path where you want to save the videos:

    ```
    Enter your download path: <your-download-path>
    ```

4. Choose the resolution for downloading (high/low/audio):

    ```
    Choose resolution (high/low/audio): <your-choice>
    ```

5. The script will start downloading the playlist videos to the specified path.

## Example

```bash
$ python Download youtube playlist .py
Enter the YouTube playlist URL: https://www.youtube.com/playlist?list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ
Enter your download path: /path/to/download
Choose resolution (high/low/audio): high
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## Acknowledgments

- [pytube](https://github.com/pytube/pytube) - A lightweight, dependency-free Python library for downloading YouTube videos.
```
