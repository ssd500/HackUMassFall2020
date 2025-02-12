import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-top-read playlist-modify-public"
ranges = ['short_term', 'medium_term', 'long_term']

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = "326a452a53254fa9bc90368567c70861", client_secret = "7d518966cb804f019a4301db077c1c31", redirect_uri = "http://localhost:8888/callback", scope = scope))

for sp_range in ['short_term', 'medium_term', 'long_term']:
    print("range:", sp_range)

    results = sp.current_user_top_artists(time_range=sp_range, limit=50)

    print(results)

    for i, item in enumerate(results['items']):
        print(i, item['name'])
    print()

if feeling == 'happy':
	if (valence lies between 0.8 and 1) and (danceability > 0.5) and (energy > 0.3):
		append that song