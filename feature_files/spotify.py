import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


class SpotifyFeature:
    is_spotify_access_ready = False

    def __init__(self, api_credentials_file, log_user_in=False, redirect_uri=""):
        with open(api_credentials_file, "r") as file:
            for i, line in enumerate(file.readlines()):
                if i == 0:
                    self.client_id = line.strip()
                elif i == 1:
                    self.client_secret = line.strip()
        if log_user_in:
            self.spotify_access = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                    client_id=self.client_id,
                    client_secret=self.client_secret,
                    redirect_uri=redirect_uri,
                    scope="user-read-playback-state,user-modify-playback-state,user-read-currently-playing"
                )
            )
            self.is_spotify_access_ready = True
        else:
            print(self.client_id)
            print(self.client_secret)
            self.spotify_access = spotipy.Spotify(
                auth_manager=SpotifyClientCredentials(
                    client_id=self.client_id, client_secret=self.client_secret
                )
            )
            self.is_spotify_access_ready = True

    def search_music(self, query, nb_results=20):
        results = self.spotify_access.search(q=query, limit=nb_results)
        return "\n".join(
            [str(index) + " - " + track["name"]
                for index, track in enumerate(results["tracks"]["items"])]
        )

    def play_music(self, uris: list):
        devices = self.spotify_access.devices()["devices"]
        if len(devices) == 0:
            return {"Error": "No device running Spotify"}
        else:
            self.spotify_access.start_playback(uris=uris)


def test_feature(api_keys_path):
    spotify = SpotifyFeature(api_keys_path, True, "http://localhost:4321")
    spotify.play_music([input("track uri: ")])


if __name__ == "__main__":
    test_feature("C:/API keys/spotify.txt")
