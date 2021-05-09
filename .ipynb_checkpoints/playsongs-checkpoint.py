import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

username = 'siddhantdubey'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']


track = spotifyObject.current_user_playing_track()
print(json.dumps(track, sort_keys=True, indent=4))
print()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist !="":
    print("Currently playing " + artist + " - " + track)

user = spotifyObject.current_user()
displayName = user['display_name']
follower = user['followers']['total']

results = spotifyObject.search(q="artist:" + "james bay" + " track: " + "let it go", type='track')


items = results['tracks']['items'][0]['uri']

spotifyObject.start_playback(deviceID, None, [items])