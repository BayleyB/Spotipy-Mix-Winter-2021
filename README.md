# README for SpotipyProject

**Last Updated: 12/20/2021**

**Basic Description:**

This program utilizes the Spotipy Python library to generate a playlist of 100 songs based off of the users top artists in Spotify. 
Everytime the program is run a new playlist is generated.

**Files:**

The following is a list of files in the project folder and a description of them.

**Code Files:**
- SpotipyProject.py: This is the main code file for the program.

**Extra Files:**
- README: Contains program description, file description, usage, and information referenced in the creation of this program.

**Usage:**
- Install Spotipy package.
- Update the code file with your Client ID, Client Secret, and Redirect URI.
- Run SpotipyProject file and a new playlist will be created on your Spotify account

**References:**

The following sources were referenced in the creation of this program. A short description of why they were referenced is below each source.

**Spotipy Docs**

https://spotipy.readthedocs.io/en/2.19.0/
This is the docs for the Spotipy python library that utilizes the Spotify API. This was referenced to understand how to create an authorization token 
which gives access to certain aspects of your Spotify account and what functions are made availiable to the developer.

**Spotify API Authorization Scopes**

https://developer.spotify.com/documentation/general/guides/authorization/scopes/#playlist-modify-private
This was referenced to understand the Spotify authorization scopes we needed to use to properly implement our program.
