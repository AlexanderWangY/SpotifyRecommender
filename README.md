# Spotify Playlist Song Recommender

A simple Python program to recommend songs for a Spotify playlist based on the song genres within it. This tool uses the Spotify API through spotipy to analyze the genres of songs in your playlist and suggests similar songs that match those genres.



## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed.
- Spotify account
- Public playlists (Spotify doesnt allow private playlists to be accessed)

## Installation

If you run this through a IDE make sure to run pip install in your terminal to get the spotipy module.

Running this straight in terminal does not work yet.

```pip install spotipy --upgrade```

Also head to [Spotify Developer Portal](https://developer.spotify.com/) and make an account. Set up your app in accordance with the documentation then input **Your client ID and Client Secret** into the ```credentials.py``` file.

Make sure to enter your username correctly (no spaces or anything extra)!


## License

This project is licensed under the [MIT License](LICENSE).

---

**Note**: This project is for educational purposes and personal use. It is not intended for commercial or production use. Use at your own risk.
