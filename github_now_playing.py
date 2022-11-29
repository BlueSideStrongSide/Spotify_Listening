from source.auth.spotify_oauth_authorization import OauthSpotify_Authorization_Code_Flow
from source.interact.spotify_api import SpotifyHandler
import pprint

spotify_authenticator = OauthSpotify_Authorization_Code_Flow(scopes=["playlist-modify-public","playlist-modify-private"], enable_env_write=False)

def main():
    if spotify_authenticator.authenticated:
        spotify_interact = SpotifyHandler(auth_manager=spotify_authenticator)

        return spotify_interact.spotify_currently_playing()


def export_to_file(api_result):
    print("Attemtping To Export")

    with open("github_now_playing.txt",mode="a+") as export_file:
        pprint.pprint(api_result, export_file)


if __name__ == '__main__':
    api_result = main()
    pprint.pprint(result, compact=True)
    export_to_file(api_result)
