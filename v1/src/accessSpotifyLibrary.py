import os
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


def init():
    load_dotenv()  # Uses Dotenv package to load variables from .env file into os variables
    scope = 'user-library-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


def printListOfSongTitles(items):
    for index, item in enumerate(items):
        print("Track {index}: {name}, by {artist}".format(index=index, name=item['track']['name'], artist=item['track']['artists'][0]['name']))


def createCSVOfLibrary(items):
    print(items[0])
    songs = []
    for item in items:
        songTitle = item['track']['name']
        songArtist = item['track']['artists'][0]['name']
        album = item['track']['album']['name']
        dateAdded = item['added_at']
        url = item['track']['external_urls']['spotify']
        if len(url > 1): url = url[0]
        uri = item['track']['uri']
        songs.append([songTitle, songArtist, album, dateAdded, url, uri]) 
    songsDF = pd.DataFrame(songs, columns=["Song_title", "Primary_artist", "Album", "Date_added", "URL", "URI"])
    print(list(songsDF["URL"]))


def accessSpotifyLibrary():
    #print("To implement accessSpotifyLibrary()")
    sp = init()
    results = sp.current_user_saved_tracks(limit=20)
    items = []
    items += results['items']
    '''
    while True:
        results = sp.next(results)
        if results is None:
            print("DONE")
            break
        #print("Results: {results}".format(results=results))
        items += results['items'] # returns just the values from the key,value pairs in results
        #print("Total: {numTracks}".format(numTracks=items[0]['track']['total']))
    '''
    #printListOfSongTitles(items)
    createCSVOfLibrary(items)

    return


if __name__ == "__main__":
    accessSpotifyLibrary()