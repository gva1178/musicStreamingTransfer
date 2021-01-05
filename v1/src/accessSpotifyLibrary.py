import os
import pandas as pd
import time
import datetime
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth



def init():
    load_dotenv()  # Uses Dotenv package to load variables from .env file into os variables
    scope = 'user-library-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


def getUserSpotifyObject():
    sp = init()
    return sp


def getSpotifyLibrarySongsList(sp):
    results = sp.current_user_saved_tracks(limit=50)
    songItems = []
    while results is not None:
        songItems += results['items'] # returns just the values from the key,value pairs in results
        results = sp.next(results)
    return songItems


def printListOfSongTitles(items):
    for index, item in enumerate(items):
        print("Track {index}: {name}, by {artist}".format(index=index, name=item['track']['name'], artist=item['track']['artists'][0]['name']))
    return


def getLibraryDF(items):
    songs = []
    for item in items:
        songTitle = item['track']['name']
        songArtist = item['track']['artists'][0]['name']
        album = item['track']['album']['name']
        dateAdded = item['added_at']
        url = item['track']['external_urls']['spotify']
        uri = item['track']['uri']
        spotify_id = item['track']['id']
        isrc = item['track']['external_ids']['isrc']
        duration_ms = item['track']['duration_ms']
        explicit = item['track']['explicit']
        songs.append([songTitle, songArtist, album, dateAdded, url, uri, spotify_id, isrc, duration_ms, explicit]) 
    songsDF = pd.DataFrame(songs, columns=["Song_title", "Primary_artist", "Album", "Date_added", "URL", "URI", "Spotify_ID", "ISRC", "Duration_(ms)", "Explicit"])
    print(songsDF[["Song_title", "Spotify_ID", "ISRC", "Duration_(ms)", "Explicit"]])
    return songsDF


'''
def getLibraryCSV(df=None, songItems=None, write_to_file=False, file_name=None):
    
    if df is None:
        if songItems is not None: df = getLibraryDF(songItems)
        else:
            print("Error: must give 'getLibraryCSV' a song library DataFrame or a list of Spotify Song Objects") 
            return None
    
    if(write_to_file):
        if file_name is None: file_name = "spotify_library_backup_{datetime}.csv".format(datetime=datetime.datetime.now())
        df.to_csv(df, file_name)
        libraryCSV = None
    else:
        libraryCSV = df.to_csv()
    
    return libraryCSV
'''


def writeLibraryDFToCSV(df=None, file_name=None):
    if file_name is None: file_name = "spotify_library_backup_{datetime}.csv".format(pwd=pwd, datetime=datetime.datetime.now())
    df.to_csv(file_name)
    return


def accessSpotifyLibrary():
    sp = getUserSpotifyObject()
    #start = time.time()
    songItems = getSpotifyLibrarySongsList(sp)
    #end = time.time()
    #print("TIME: {time}".format(time=(start-end)))
    #printListOfSongTitles(songItems)
    library_DF = getLibraryDF(songItems)
    #writeLibraryDFToCSV(library_DF)
    #getLibraryCSV(df=library_DF, write_to_file=True)
    return


if __name__ == "__main__":
    accessSpotifyLibrary()