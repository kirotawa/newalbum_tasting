# -*- coding: utf-8 -*-

import urllib
import urllib2
import simplejson
from BeautifulSoup import BeautifulSoup

# Constants
URL_ALBUMS_RELEASE = "http://newalbumreleases.net/category/indie/"
URL_TINYSONG = "http://tinysong.com/s/%s?format=json&limit=3&key=%s"
API_KEY = "41ec844123da671b3f7427eab2f97734" #"63fe319e7dc204b384e875bb28c70671"

def get_new_albums():
    request = urllib2.Request(URL_ALBUMS_RELEASE, headers={'User-Agent': "Magic Browser"})
    response = urllib2.urlopen(request)
    
    document = response.read()
    soup = BeautifulSoup(document)

    all_data_albums = soup.findAll('div', {'class':'single'})
    artists = []
    
    for artist in all_data_albums:
        artists.append(artist.find('b').next)

    return artists


def get_songs_artist(artist):
    artist_encode = urllib.quote(artist)
    url_ = URL_TINYSONG % (artist, API_KEY)
    request = urllib2.Request(URL_TINYSONG % (artist_encode, API_KEY))
    response = urllib2.urlopen(request)

    document = response.read()
    artist_songs = simplejson.loads(document)

    return artist_songs


def load_artist_songs():
    artists_songs = []
    for artist in get_new_albums():
        arts_songs = get_songs_artist(artist)
        try:
            if artist == arts_songs[0]['ArtistName']:
                artists_songs.append(arts_songs)
        except:
            pass
    return artists_songs





