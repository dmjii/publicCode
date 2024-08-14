# This program will not make any changes as-is (safe preview mode). 
# After you have previewed your output using lines 95-99, comment out 
# lines 95-99 and UNCOMMENT line 93 to write your bulk playlist 
# changes (WARNING!) to your Spotify account! Use at your own risk.
import sys
import textwrap
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = 'Your_Spotify_Developer_Account_Client_ID_Goes_Here'
SPOTIPY_CLIENT_SECRET = 'Your_Spotify_Developer_Account_Client_Secret_Goes_Here'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = 'user-library-read playlist-read-private playlist-modify-public playlist-modify-private'
# Authenticate the user
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))
count = 0
# Retrieve playlists
def get_playlists():
    playlists = []
    offset = 0
    limit = 50  # The number of playlists to retrieve per request, adjust as needed

    while True:
        results = sp.user_playlists(sp.me()['id'], limit=limit, offset=offset) #results is a dictionary
        playlists.extend(results['items']) #add value of 'items' to playlists (contains name etc.)
        offset += limit
        if len(results['items']) == 0:  # No more playlists to retrieve
            break 

    return playlists

# Remove "-2023" endings from playlist names - a consequence of third party importing... # Change as needed
def clean_playlist_names(playlists):
    cleaned_playlists = []
    final_playlists = []
    for playlist in playlists:
        name = playlist['name']
        if "-2023" in name:
            index = name.find("-2023")
            if index != -1:
                cleaned_name = name[:index]
                #keep all playlist info in tuple associated with new name
                cleaned_playlists.append((playlist, cleaned_name)) 
        else:
            cleaned_playlists.append((playlist, name))
    
    for prep_playlists in cleaned_playlists: #changing the "V" to "v" in all my "cycling vol" playlists...
        almosts = prep_playlists[1]
        if "Cycling Vol" in almosts:
            indexc = almosts.find("Vol")
            if indexc != -1:
                final_names = almosts[:indexc] + str.lower(almosts[indexc]) + almosts[indexc+1:]
                final_playlists.append((prep_playlists,final_names))
        else:
            final_playlists.append((prep_playlists, almosts))  
    return final_playlists

# Update playlist titles
def update_playlist_titles(playlists):
    user_id = sp.me()['id'] #get the authenticated user id
    for playlist, new_title in playlists:
        if playlist[0]['owner']['id'] == user_id:
            sp.user_playlist_change_details(
                sp.me()['id'], #retrieves user's authenticated Spotify ID
                playlist[0]['id'],
                name=new_title #changes name to the altered title
            )
            print(f"Updated playlist title to: {new_title}")
        else:
            print(f"Skipped playlist '{playlist[1]}' because it's not a playlist you own")

if __name__ == "__main__":
    welcome_message = "Welcome to the Playist Bulk Editor/Deleter App {0}" .format(sp.me()['display_name'])
    bars = "********************************************"
    print(bars)
    print(welcome_message)
    print(bars)
    purpose = """The purpose of this app is to delete text that may have been tagged to the end of 
    your playlist unintentionally by import automation. In this case an importer application tagged all 
    imported playlists with the date, adding '-2023' to the ending of the playlist name. This tagging 
    will be removed in this program. Future developments may include a different term to search for and delete."""
    agree = "Do you agree to run this program? (y/n):"
    paragraph_width = 60
    paragraphs = textwrap.wrap(purpose, width= paragraph_width)
    for paragraph in paragraphs:
        print(paragraph)
    print(bars)
    answer = input(agree)
    if (answer == 'y'):
        playlists = get_playlists()
        final_playlists = clean_playlist_names(playlists)
        # update_playlist_titles(final_playlists) #WARNING

        # Use the below code to preview your playlist ID's before updating to Spotify!!
        for playlists in final_playlists:
            count += 1
            print(playlists[1])
        print(count)
    else:
        sys.exit()

# This program will not make any changes as-is (safe preview mode). 
# After you have previewed your output using lines 95-99, comment out 
# lines 95-99 and UNCOMMENT line 93 to write your bulk playlist 
# changes (WARNING!) to your Spotify account! Use at your own risk.