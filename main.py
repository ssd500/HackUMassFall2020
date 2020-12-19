# Our HackUMass2020 code will go into here! Yippee! Yeet! Beep ! Woot!
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-top-read playlist-modify-public"

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


def get_mean_valence(sp, top_tracks_uri)
    track_Valence = []
    median_Valence = 0
    stdev_Valence = 0
    for tracks in top_tracks_uri:
        tracks_all_data = sp.audio_features(tracks)
        for track_data in tracks_all_data
            track_valence.append(track_data["valence"])
        mean_Valence = statistics.mean(track_Valence)
        stdev_Valence = statistics.stdev(track_Valence)

    return mean_Valence, stdev_Valence

def get_mean_tempo(sp, top_tracks_uri)
    track_Tempo = []
    mean_Tempo = 0
    stdev_Tempo = 0
    for tracks in top_tracks_uri:
        tracks_all_data = sp.audio_features(tracks)
        for track_data in tracks_all_data
            track_Tempo.append(track_data["tempo"])
        mean_Tempo = statistics.mean(track_Tempo)
        stdev_Tempo = statistics.stdev(track_Tempo)
    return mean_Tempo, stdev_Tempo

def get_mean_energy(sp, top_tracks_uri)
    track_Energy = []
    mean_Energy = 0
    stdev_Energy = 0
    for tracks in top_tracks_uri:
        tracks_all_data = sp.audio_features(tracks)
        for track_data in tracks_all_data
            track_Energy.append(track_data["energy"])
        mean_Energy =  statistics.mean(track_Energy)
        stdev_Energy = statistics.stdev(track_Energy)
    return mean_Energy, stdev_Energy


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

find mean_valence, mean_tempo, mean_energy
find stddev_valence, stddev_tempo, stddev_energy
for example, high_valence = all valence greater than equal to mean_valence + stddev_valence
medium_valence = all valence between mean_valence - stddev_valence & mean_valence + stddev_valence
low_valence = all valence lesser than mean_valence - stddev_valence
u might wanna do weighted sum like mean_valence + 0.5 * stddev_valence 
or mean_valence + 0.25 * stddev_valence 
depending on how much data you want distributed for each categories
