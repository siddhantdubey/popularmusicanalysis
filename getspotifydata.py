import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

songdata = pd.read_csv('charts.csv')

uniquesongdata = songdata.drop_duplicates(subset='song')

# #we want to keep only unique songs which is what the above code does

# genres = []

# for artist in uniquesongdata['artist']:
#     try:
#         result = sp.search(artist)
#         track = result['tracks']['items'][0]
#         artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
#         print("artist genres:", artist["genres"])
#         album = sp.album(track["album"]["external_urls"]["spotify"])
#         print("album genres:", album["genres"])
#         print("album release-date:", album["release_date"])

#         genres.append(artist['genres'])
#     except:
#         genres.append('genre not found')

result = sp.search("NF")
track = result['tracks']['items'][0]

artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
print("artist genres:", artist["genres"])

album = sp.album(track["album"]["external_urls"]["spotify"])
print("album genres:", album["genres"])
print("album release-date:", album["release_date"])

# uniquesongdata['genre'] = genres

# uniquesongdata.to_csv('datawithgenre.csv')

# results = sp.search(q="artist:" + "james bay" + " track: " + "let it go", type='track')

# with open('results.json', 'w+') as outfile:
#     json.dump(results, outfile)

# items = results['tracks']['items'][0]['uri']

# print(sp.track(items)['genre'])


