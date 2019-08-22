import signal
import spotipy, spotipy.util as util
import numpy as np
from data.dataitem import DataItem

client_key = 'b4847d3dd2464848bc7f1f34b04f9509'
secret_key = '1ebd017edc044803906b36e81bd48cc3'
url        = 'http://localhost:8888/callback/'

username   = 'sharpieman20'
scopes     = [
'user-top-read',
'user-read-recently-played',
'user-read-playback-state',
'user-read-currently-playing',
'user-modify-playback-state',
'user-library-modify',
'user-library-read',
'streaming',
'app-remote-control',
'user-read-private',
'user-read-email',
'user-follow-modify',
'user-follow-read',
'playlist-modify-public',
'playlist-read-collaborative',
'playlist-read-private',
'playlist-modify-private']
scope = ' '.join(scopes)

# TODO: Replace spotipy's authentication process with your own
def get_spotify_permissions():
	token = util.prompt_for_user_token(username,scope,client_id=client_key,client_secret=secret_key,redirect_uri=url)
	global spotify
	spotify = spotipy.Spotify(auth=token)

def get(type, id):
	if type == 'album':
		data = spotify.album(id)
	elif type == 'song':
		data = spotify.track(id)
	return DataItem.create_item(type, 'spotify', data)

def search(type, name):
	search_results = spotify.search(type + ': ' + name, limit=1,type=type)
	id = search_results[type + 's']['items'][0]['id']
	return get(type, id)

def current():
	cur = spotify.currently_playing()
	song = DataItem.create_item('song', 'spotify-current', cur)
	return song

def pause_player():
	spotify.pause_playback()

def unpause_player():
	spotify.start_playback()

# def to_local(data):
# 	temp = []
# 	if 'album_type' in data.keys():
# 		temp.append(data['id'])
# 		temp.append(data['name'])
# 		temp.append([track['id'] for track in data['tracks']['items']])
# 	else:
# 		temp.append(data['id'])
# 		temp.append(data['name'])
# 		temp.append(data['artists'][0]['name'])
# 		temp.append([])
# 		temp.append([])
# 	return temp