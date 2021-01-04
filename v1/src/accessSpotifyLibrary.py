import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


def init():
    load_dotenv()  # Uses Dotenv package to load variables from .env file into os variables
    scope = 'user-library-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


def accessSpotifyLibrary():
    #print("To implement accessSpotifyLibrary()")
    sp = init()
    results = sp.current_user_saved_tracks(limit=20)
    items = []
    while True:
        results = sp.next(results)
        if results is None:
            print("DONE")
            break
        #print("Results: {results}".format(results=results))
        items += results['items'] # returns just the values from the key,value pairs in results
        #print("Total: {numTracks}".format(numTracks=items[0]['track']['total']))
    for index, item in enumerate(items):
        print("Track {index}: {name}, by {artist}".format(index=index, name=item['track']['name'], artist=item['track']['artists'][0]['name']))
        #print(item)
   
    return


if __name__ == "__main__":
    accessSpotifyLibrary()