# Our HackUMass2020 code will go into here! Yippee! Yeet! Woot!
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-top-read playlist-modify-public"
ranges = ['short_term', 'medium_term', 'long_term']

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = "326a452a53254fa9bc90368567c70861", client_secret = "7d518966cb804f019a4301db077c1c31", redirect_uri = "http://localhost:8888/callback", scope = scope))

def get_top_artists(sp):
    
    results = sp.current_user_top_artists(time_range = "short_term", limit = 15)
    
    return results['items']

def get_top_tracks(sp, top_artists):
    
    top_tracks_uri = []
    for i in top_artists:
        top_tracks_all_data = sp.artist_top_tracks(i)
        top_tracks_data = top_tracks_all_data['tracks']
        for track_data in top_tracks_data:
            top_tracks_uri.append(track_data['uri'])
    
    return top_tracks_uri





if feeling == 'happy':
	if (valence lies between 0.8 and 1) and (danceability > 0.5) and (energy > 0.3):
		append that song

if feeling == 'happy':
    if (valency + danceability + energy > 1.5):
        append

if feeling == 'happy':
    if (valency * 0.7 + danceability * 0.2 + energy *0.1 > 1):
        append

get the mean and standard deviation for all songs
then everything above mean + std dev is happy
mean - std dev to mean + std dev is neutral
below mean - std dev is sad
