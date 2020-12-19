# Our HackUMass2020 code will go into here! Yippee! Yeet! Beep ! Woot!
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-top-read playlist-modify-public"

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = "326a452a53254fa9bc90368567c70861", client_secret = "7d518966cb804f019a4301db077c1c31", redirect_uri = "http://localhost:8888/callback", scope = scope))

def get_top_artists(sp):
    
    top_artists = sp.current_user_top_artists(time_range = "short_term", limit = 15)
    
    top_artists_uri = []

    for i in top_artists["items"]:
        top_artists_uri.append(i["uri"])

    return top_artists_uri

def get_top_tracks(sp, top_artists):
    
    top_tracks_uri = []
    for i in top_artists:
        top_tracks_all_data = sp.artist_top_tracks(i)
        top_tracks_data = top_tracks_all_data['tracks']
        for track_data in top_tracks_data:
            top_tracks_uri.append(track_data['uri'])
    
    return top_tracks_uri


def get_valence(sp, top_tracks_uri):

    for tracks in top_tracks_uri:
        tracks_all_data = sp.audio_features(tracks)
        for track_data in tracks_all_data:
            track_valence.append(track_data["valence"])

def get_mean_Valence(track_Valence):
    
    return mean_Valence = statistics.mean(track_Valence)

def get_stdev_Valence(track_Valence):
    
    return stdev_Valence = statistics.stdev(track_Valence)


def get_tempo(sp, top_tracks_uri):
    
    for tracks in top_tracks_uri:
        tracks_all_data = sp.audio_features(tracks)
        for track_data in tracks_all_data
            track_Tempo.append(track_data["tempo"])

def get_mean_Tempo(track_Tempo):      
    
    return mean_Tempo = statistics.mean(track_Tempo)

def get_stdev_Tempo(track_Tempo):
    
    return stdev_Tempo = statistics.stdev(track_Tempo)


def get_energy(sp, top_tracks_uri):
    
    for tracks in top_tracks_uri:
        tracks_all_data = sp.audio_features(tracks)
        for track_data in tracks_all_data
            track_Energy.append(track_data["energy"])

def get_mean_Energy(track_Energy):
    
    return mean_Energy = statistics.mean(track_Energy)

def get_stdev_Energy(track_Energy):
    
    return stdev_Energy = statistics.stdev(track_Energy)

# high_valence = all valence greater than equal to mean_valence + stddev_valence

# medium_valence = all valence between mean_valence - stddev_valence & mean_valence + stddev_valence

# low_valence = all valence lesser than mean_valence - stddev_valence

# Mellow - Major, High valence, Low tempo, Low energy
# Melancholy - Minor, low valence, Low tempo, Low energy

# Happy - Major, high valence, medium tempo, medium energy
# Sad - Minor, low valence, medium tempo, medium energy

# Cheerful- Major, High valence, High tempo, High energy
# Angry - Minor, low valence, High tempo, High energy


def select_the_tracks(sp, top_tracks_uri, mood):
    selected_tracks_uri = []
    for tracks in top_tracks_uri:
        tracks_all_data = sp.audio_features(tracks)
        for track_data in tracks_all_data:
            try:
                for mood in moods:
                    if mood == "Mellow":
                        if(track_data["mode"] == 1
                        and track_data["valence"] >= (mean_Valence + stdev_Valence)
                        and track_data["tempo"] < (mean_Tempo - stdev_Tempo)
                        and track_data["energy"] < (mean_Energy - stdev_Energy))
                            selected_tracks_uri.append(track_data["uri"])
                    elif mood == "Melancholy":
                        if(track_data["mode"] == 0
                        and track_data["valence"] < (mean_Valence - stdev_Valence)
                        and track_data["tempo"] < (mean_Tempo - stdev_Tempo)
                        and track_data["energy"] < (mean_Energy - stdev_Energy))
                            selected_tracks_uri.append(track_data["uri"])
                    elif mood == "Happy":
                        if(track_data["mode"] == 1
                        and track_data["valence"] >= (mean_Valence + stdev_Valence)
                        and ((mean_Tempo - stdev_Tempo) < track_data["tempo"] < (mean_Tempo + stdev_Tempo))
                        and ((mean_Energy - stdev_Energy) < track_data["energy"] < (mean_Energy + stdev_Energy))
                            selected_tracks_uri.append(track_data["uri"])
                    elif mood == "Sad":
                        if(track_data["mode"] == 0
                        and track_data["valence"] < (mean_Valence - stdev_Valence)
                        and ((mean_Tempo - stdev_Tempo) < track_data["tempo"] < (mean_Tempo + stdev_Tempo))
                        and ((mean_Energy - stdev_Energy) < track_data["energy"] < (mean_Energy + stdev_Energy))
                            selected_tracks_uri.append(track_data["uri"])
                    elif mood == "Cheerful":
                        if(track_data["mode"] == 1
                        and track_data["valence"] >= (mean_Valence + stdev_Valence)
                        and track_data["tempo"] >= (mean_Tempo + stdev_Tempo)
                        and track_data["energy"] >= (mean_Energy + stdev_Energy))
                            selected_tracks_uri.append(track_data["uri"])
                    elif mood == "Angry":
                        if(track_data["mode"] == 0
                        and track_data["valence"] < (mean_Valence - stdev_Valence)
                        and track_data["tempo"] >= (mean_Tempo + stdev_Tempo)
                        and track_data["energy"] >= (mean_Energy + stdev_Energy))
                            selected_tracks_uri.append(track_data["uri"])
                except TypeError as type_e:
                    ConnectionRefusedError

    return selected_tracks_uri

			   
###
        

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
