import spotipy
from spotipy.oauth2 import SpotifyOAuth
from random import randrange

#user values
SPOTIPY_CLIENT_ID = 'YOUR-ID-HERE'
SPOTIPY_CLIENT_SECRET = 'YOUR-CLIENT-SECRET'
SPOTIPY_REDIRECT_URI = 'https://placeholder.github.io/'

#define scope
scope = "user-read-private playlist-modify-public user-top-read"

#create spotipy object
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=scope))

#globals
name = "Spotipy Daily Mix"
description = "Playlist of 100 songs related to your top artists"
playlistID = ""
artistList = []
IDList = []

#get user values
values = spotify.current_user()

#get username
user = values["uri"].replace("spotify:user:", "")

#create playlist and grab uri
newPlaylist = spotify.user_playlist_create(user = user, name = name, description = description)
playlistID = newPlaylist["uri"].replace("spotify:playlist:", "")

#get followed artists
artists = spotify.current_user_top_artists(limit=5)

#get followed artists ID
artists = artists["items"]
for artist in artists:
	artistID = artist["uri"].replace("spotify:artist:", "")
	artistList.append(artistID)

#get related artists of followed artists
for artist in artistList:
	relatedArtists = spotify.artist_related_artists(artist)
	relatedArtists = relatedArtists["artists"]

	#adds random song from each related artist
	for relatedArtist in relatedArtists:
		artistID = relatedArtist["uri"].replace("spotify:artist:", "")
		topTracks = spotify.artist_top_tracks(artistID)
		topTracks = topTracks["tracks"]
		randomNumber = randrange(len(topTracks) - 1)
		topTracks = topTracks[randomNumber]
		songID = topTracks["uri"].replace("spotify:track:", "")
		IDList.append(songID)

#adds songs to playlist
spotify.playlist_add_items(playlistID, IDList)
		