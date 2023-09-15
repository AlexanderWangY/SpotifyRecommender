import random
import spotipy
import credentials
from spotipy.oauth2 import SpotifyClientCredentials


if __name__ == '__main__':
        # Authorizing the app in spotify tools, the app credentials are stored seperately in credentials.py
        cred_initialize = SpotifyClientCredentials(client_id=credentials.client_id,
                                                   client_secret=credentials.client_SECRET)
        sp = spotipy.Spotify(auth_manager=cred_initialize)

        # UserID is the username of the user

        UserID = input("What is your Spotify username: ")

        dictPL = sp.user_playlists(UserID)

        playlistDict = {}

        for x in dictPL["items"]:
            playlistDict[x["name"]] = x["id"]

        print("Your available playlist's are:")
        for x in playlistDict:
            print(x)

        while(True):
            searchPlaylist = input("What playlist should we recommend from?\n")
            if searchPlaylist in playlistDict:
                break
            else:
                print("Playlist not found! Please try again...")

        playlistTracks = sp.user_playlist_tracks(UserID, playlist_id=playlistDict[searchPlaylist], limit=100)

        artistArr = []

        for x in playlistTracks["items"]:
            # print(x["track"])
            artistArr.append(x["track"]["artists"][0]["id"])

        genreCountDict = {}

        for x in artistArr:
            currentArtist = sp.artist(x)

            for y in currentArtist["genres"]:
                if y not in genreCountDict:
                    genreCountDict[y] = 1
                elif y in genreCountDict:
                    genreCountDict[y] += 1;

        sortedGenres = sorted(genreCountDict.items(), key=lambda x: int(x[1]))

        topGenres = []

        if len(genreCountDict) > 5:
            for x in range(5):
                topGenres.append(sortedGenres[len(sortedGenres) - (1 + x)][0])
        else:
            for x in sortedGenres:
                topGenres.append(x[0])

        print("\nWe think you'll like...\n")

        for genres in topGenres:
            randomIndex = random.randint(0, 50)
            try:
                currentTrack = sp.search(q=f"genres:{genres}", limit=50)["tracks"]["items"][randomIndex]
                print(f"{currentTrack['name']} by: {currentTrack['artists'][0]['name']}")
            except IndexError:
                print()

        print("\nThank you for using my program!")
