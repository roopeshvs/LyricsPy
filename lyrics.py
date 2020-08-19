# Get lyrics delivered to your CLI

import requests, sys
from bs4 import BeautifulSoup, Comment

def lyrics_find(Artist, Song):
    # Base URL to build on
    URL = 'https://www.azlyrics.com/lyrics/'

    # Modify Artist Name and Song Title to URL Format
    Artist = Artist.lower().replace(" ","")
    Song = Song.lower().replace(" ","")

    # So our Bot doesn't get classified as a Bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    # Get Page from AZLyrics.
    # Raise Exception If Page doesn't exist.
    try:
        page = requests.get(URL+'/'+Artist+'/'+Song+'.html', headers=headers)
        if not page:
            raise Exception(page.status_code)
    except Exception as err:
        print("Cannot Find Song. Please Check The Artist's Name and Song Title. Response Status Code: " + str(err))
        return page.status_code

    # Parse HTML to Soup
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find All Divs With No Class Name
    div_with_no_names = soup.findAll('div', class_=None)

    # Find Lyrics Div From All Divs
    for index, divs in enumerate(div_with_no_names):
        if index == 1:
            # Remove Unnecessary Tags
            print(divs.text)
            print('Lyrics From AZLyrics @ '+URL+Artist+'/'+Song)
            return page.status_code

if __name__ == "__main__":
    # Get Artist Name and Song Title
    Artist = input("Artist: ")
    Song = input("Song Title: ")
    lyrics_find(Artist, Song)
