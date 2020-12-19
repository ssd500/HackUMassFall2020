# Our HackUMass2020 code will go into here! Yippee! Yeet! Woot!
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-top-read playlist-modify-public"
ranges = ['short_term', 'medium_term', 'long_term']

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = "326a452a53254fa9bc90368567c70861", client_secret = "7d518966cb804f019a4301db077c1c31", redirect_uri = "http://localhost:8888/callback", scope = scope))

def get_top_artists(sp):
    
    results = sp.current_user_top_artists(time_range = "short_term", limit = 15)
    
    return results['items']

get_top_artists(sp)
