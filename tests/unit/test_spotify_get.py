import pytest
import json
from source.auth.spotify_oauth_authorization import OauthSpotify_Authorization_Code_Flow
from source.interact.spotify_endpoint_results import  SpotifyTrackResult
from source.interact.spotify_api import SpotifyHandler


@pytest.fixture
def sample_track_data():
    # will remove in a future update
    internal_sample_track_json = {"tracks": [{"album": {"album_type": "album", "artists": [
        {"external_urls": {"spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"},
         "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI", "id": "12Chz98pHFMPJEknJQMWvI",
         "name": "Muse", "type": "artist", "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"}],
                           "available_markets": ["AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BB",
                                                 "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR", "BS", "BT",
                                                 "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CL", "CM", "CO", "CR",
                                                 "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE",
                                                 "EG", "ES", "FI", "FJ", "FM", "FR", "GA", "GB", "GD", "GE", "GH", "GM",
                                                 "GN", "GQ", "GR", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID",
                                                 "IE", "IL", "IN", "IQ", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH",
                                                 "KI", "KM", "KN", "KR", "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR",
                                                 "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MH", "MK",
                                                 "ML", "MN", "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA",
                                                 "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG",
                                                 "PH", "PK", "PL", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RW", "SA",
                                                 "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR", "ST", "SV",
                                                 "SZ", "TD", "TG", "TH", "TJ", "TL", "TN", "TO", "TR", "TT", "TV", "TW",
                                                 "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VE", "VN", "VU", "WS", "XK",
                                                 "ZA", "ZM", "ZW"],
                           "external_urls": {"spotify": "https://open.spotify.com/album/0lw68yx3MhKflWFqCsGkIs"},
                           "href": "https://api.spotify.com/v1/albums/0lw68yx3MhKflWFqCsGkIs",
                           "id": "0lw68yx3MhKflWFqCsGkIs", "images": [
            {"height": 640, "url": "https://i.scdn.co/image/ab67616d0000b27328933b808bfb4cbbd0385400", "width": 640},
            {"height": 300, "url": "https://i.scdn.co/image/ab67616d00001e0228933b808bfb4cbbd0385400", "width": 300},
            {"height": 64, "url": "https://i.scdn.co/image/ab67616d0000485128933b808bfb4cbbd0385400", "width": 64}],
                           "name": "Black Holes and Revelations", "release_date": "2006-06-19",
                           "release_date_precision": "day", "total_tracks": 12, "type": "album",
                           "uri": "spotify:album:0lw68yx3MhKflWFqCsGkIs"}, "artists": [
        {"external_urls": {"spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"},
         "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI", "id": "12Chz98pHFMPJEknJQMWvI",
         "name": "Muse", "type": "artist", "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"}],
                 "available_markets": ["AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ",
                                       "DK", "DO", "DE", "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU",
                                       "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO",
                                       "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR",
                                       "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL", "ZA",
                                       "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS",
                                       "IN", "BY", "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "KR",
                                       "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ",
                                       "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT",
                                       "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW",
                                       "PG", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL",
                                       "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ",
                                       "GA", "GN", "KG", "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ",
                                       "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE",
                                       "ET", "XK"], "disc_number": 1, "duration_ms": 366213, "explicit": False,
                 "external_ids": {"isrc": "GBAHT0500600"},
                 "external_urls": {"spotify": "https://open.spotify.com/track/7ouMYWpwJ422jRcDASZB7P"},
                 "href": "https://api.spotify.com/v1/tracks/7ouMYWpwJ422jRcDASZB7P", "id": "7ouMYWpwJ422jRcDASZB7P",
                 "is_local": False, "name": "Knights of Cydonia", "popularity": 71,
                 "preview_url": "https://p.scdn.co/mp3-preview/8196f1d0cb4c14a5a5bd1ab078c6893b30dab102?cid=0b297fa8a249464ba34f5861d4140e58",
                 "track_number": 11, "type": "track", "uri": "spotify:track:7ouMYWpwJ422jRcDASZB7P"}, {
                    "album": {"album_type": "album", "artists": [
                        {"external_urls": {"spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"},
                         "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                         "id": "12Chz98pHFMPJEknJQMWvI", "name": "Muse", "type": "artist",
                         "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"}],
                              "available_markets": ["AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA",
                                                    "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR",
                                                    "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CL",
                                                    "CM", "CO", "CR", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM",
                                                    "DO", "DZ", "EC", "EE", "EG", "ES", "FI", "FJ", "FM", "FR", "GA",
                                                    "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GR", "GT", "GW", "GY",
                                                    "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IQ", "IS",
                                                    "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR",
                                                    "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU",
                                                    "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MN",
                                                    "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE",
                                                    "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG",
                                                    "PH", "PK", "PL", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RW",
                                                    "SA", "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR",
                                                    "ST", "SV", "SZ", "TD", "TG", "TH", "TJ", "TL", "TN", "TO", "TR",
                                                    "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VE",
                                                    "VN", "VU", "WS", "XK", "ZA", "ZM", "ZW"],
                              "external_urls": {"spotify": "https://open.spotify.com/album/0eFHYz8NmK75zSplL5qlfM"},
                              "href": "https://api.spotify.com/v1/albums/0eFHYz8NmK75zSplL5qlfM",
                              "id": "0eFHYz8NmK75zSplL5qlfM", "images": [
                            {"height": 640, "url": "https://i.scdn.co/image/ab67616d0000b273b6d4566db0d12894a1a3b7a2",
                             "width": 640},
                            {"height": 300, "url": "https://i.scdn.co/image/ab67616d00001e02b6d4566db0d12894a1a3b7a2",
                             "width": 300},
                            {"height": 64, "url": "https://i.scdn.co/image/ab67616d00004851b6d4566db0d12894a1a3b7a2",
                             "width": 64}], "name": "The Resistance", "release_date": "2009-09-10",
                              "release_date_precision": "day", "total_tracks": 11, "type": "album",
                              "uri": "spotify:album:0eFHYz8NmK75zSplL5qlfM"}, "artists": [
            {"external_urls": {"spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"},
             "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI", "id": "12Chz98pHFMPJEknJQMWvI",
             "name": "Muse", "type": "artist", "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"}],
                    "available_markets": ["AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ",
                                          "DK", "DO", "DE", "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU",
                                          "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO",
                                          "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR",
                                          "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL", "ZA",
                                          "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS",
                                          "IN", "BY", "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "KR",
                                          "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ",
                                          "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT",
                                          "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW",
                                          "PG", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL",
                                          "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ",
                                          "GA", "GN", "KG", "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ",
                                          "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE",
                                          "ET", "XK"], "disc_number": 1, "duration_ms": 304840, "explicit": False,
                    "external_ids": {"isrc": "GBAHT0900320"},
                    "external_urls": {"spotify": "https://open.spotify.com/track/4VqPOruhp5EdPBeR92t6lQ"},
                    "href": "https://api.spotify.com/v1/tracks/4VqPOruhp5EdPBeR92t6lQ", "id": "4VqPOruhp5EdPBeR92t6lQ",
                    "is_local": False, "name": "Uprising", "popularity": 77,
                    "preview_url": "https://p.scdn.co/mp3-preview/529eb48df232955cdd3b870f21e2bd41f1657fae?cid=0b297fa8a249464ba34f5861d4140e58",
                    "track_number": 1, "type": "track", "uri": "spotify:track:4VqPOruhp5EdPBeR92t6lQ"}, {
                    "album": {"album_type": "album", "artists": [
                        {"external_urls": {"spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"},
                         "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                         "id": "12Chz98pHFMPJEknJQMWvI", "name": "Muse", "type": "artist",
                         "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"}],
                              "available_markets": ["AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA",
                                                    "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR",
                                                    "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CL",
                                                    "CM", "CO", "CR", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM",
                                                    "DO", "DZ", "EC", "EE", "EG", "ES", "FI", "FJ", "FM", "FR", "GA",
                                                    "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GR", "GT", "GW", "GY",
                                                    "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IQ", "IS",
                                                    "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR",
                                                    "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU",
                                                    "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MN",
                                                    "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE",
                                                    "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG",
                                                    "PH", "PK", "PL", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RW",
                                                    "SA", "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR",
                                                    "ST", "SV", "SZ", "TD", "TG", "TH", "TJ", "TL", "TN", "TO", "TR",
                                                    "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VE",
                                                    "VN", "VU", "WS", "XK", "ZA", "ZM", "ZW"],
                              "external_urls": {"spotify": "https://open.spotify.com/album/0HcHPBu9aaF1MxOiZmUQTl"},
                              "href": "https://api.spotify.com/v1/albums/0HcHPBu9aaF1MxOiZmUQTl",
                              "id": "0HcHPBu9aaF1MxOiZmUQTl", "images": [
                            {"height": 640, "url": "https://i.scdn.co/image/ab67616d0000b2738cb690f962092fd44bbe2bf4",
                             "width": 640},
                            {"height": 300, "url": "https://i.scdn.co/image/ab67616d00001e028cb690f962092fd44bbe2bf4",
                             "width": 300},
                            {"height": 64, "url": "https://i.scdn.co/image/ab67616d000048518cb690f962092fd44bbe2bf4",
                             "width": 64}], "name": "Absolution", "release_date": "2004-03-23",
                              "release_date_precision": "day", "total_tracks": 15, "type": "album",
                              "uri": "spotify:album:0HcHPBu9aaF1MxOiZmUQTl"}, "artists": [
            {"external_urls": {"spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"},
             "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI", "id": "12Chz98pHFMPJEknJQMWvI",
             "name": "Muse", "type": "artist", "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"}],
                    "available_markets": ["AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ",
                                          "DK", "DO", "DE", "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU",
                                          "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO",
                                          "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR",
                                          "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL", "ZA",
                                          "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS",
                                          "IN", "BY", "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "KR",
                                          "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ",
                                          "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT",
                                          "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW",
                                          "PG", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL",
                                          "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ",
                                          "GA", "GN", "KG", "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ",
                                          "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE",
                                          "ET", "XK"], "disc_number": 1, "duration_ms": 237039, "explicit": False,
                    "external_ids": {"isrc": "GBCVT0300078"},
                    "external_urls": {"spotify": "https://open.spotify.com/track/2takcwOaAZWiXQijPHIx7B"},
                    "href": "https://api.spotify.com/v1/tracks/2takcwOaAZWiXQijPHIx7B", "id": "2takcwOaAZWiXQijPHIx7B",
                    "is_local": False, "name": "Time is Running Out", "popularity": 71,
                    "preview_url": "https://p.scdn.co/mp3-preview/bdfe028edf28096825284b1e8bc1ba8c2cdb28b8?cid=0b297fa8a249464ba34f5861d4140e58",
                    "track_number": 3, "type": "track", "uri": "spotify:track:2takcwOaAZWiXQijPHIx7B"}]}
    # with open("sample_track.json", 'r') as f:
    # data = json.load(internal_sample_track_json)

    return internal_sample_track_json

def test_offline_get_tracks(sample_track_data):
    result_track = [x for x in sample_track_data["tracks"]]
    assert len(result_track) == 3

def test_offline_get_tracks_track_handler(sample_track_data):
    result_track = [SpotifyTrackResult(x) for x in sample_track_data["tracks"]]
    assert result_track[0].track_name == "Knights of Cydonia"
    assert result_track[1].track_name == "Uprising"
    assert result_track[2].track_name == "Time is Running Out"

@pytest.fixture(scope="module")
def spotify_interact():
    spotify_authenticator = OauthSpotify_Authorization_Code_Flow(scopes=["user-read-recently-played", 'user-top-read'],
                                                                 enable_env_write=False)
    if spotify_authenticator.authenticated:
        return SpotifyHandler(auth_manager=spotify_authenticator)

def test_live_get_tracks(spotify_interact):
    result = spotify_interact.spotify_get_tracks(ids="7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B")
    assert len(result.tracks) == 3

def test_live_get_playlist(spotify_interact):
    result = spotify_interact.spotify_get_playlist(playlist_id="3cEYpjA9oz9GiPac4AsH4n")
    assert result.response.get("description") == 'A playlist for testing pourposes'

def test_live_get_audio_features(spotify_interact):
    result = spotify_interact.spotify_track_audio_features(spotify_id="11dFghVXANMlKmJXsNCbNl")
    assert result.response.get("instrumentalness") == 0.000905


if __name__ == '__main__':
    print("Local Testing")