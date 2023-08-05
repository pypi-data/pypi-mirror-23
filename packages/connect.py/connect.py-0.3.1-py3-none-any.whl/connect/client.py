# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2016-2017 GiovanniMCMXCIX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from .http import HTTPClient
from .errors import NotFound
from .release import Release
from .track import Track
from .artist import Artist
from .playlist import Playlist
from urllib.parse import quote


class Client:
    def __init__(self):
        self.http = HTTPClient()

    def sign_in(self, email: str, password: str, token: int=None):
        """Logs in the client with the specified credentials."""
        if not token:
            self.http.email_sign_in(email, password)
        else:
            self.http.two_feature_sign_in(email, password, token)

    @property
    def is_signed_in(self):
        """Indicates if the client has signed in successfully."""
        return self.http.is_singed_in()

    def sign_out(self):
        """Logs out of Monstercat Connect."""
        self.http.sign_out()

    def edit_profile(self, *, name: str=None, real_name: str=None, location: str=None, password: str=None):
        """Edits the current profile of the client."""
        self.http.edit_profile(name=name, real_name=real_name, location=location, password=password)

    def add_reddit_username(self, username: str):
        """Adds the reddit username to the current profile of the client."""
        self.http.add_reddit_username(username)

    def get_discord_gold_invite(self):
        """Gets an invite for the gold discord channel on the monstercat discord guild, 
        needs gold subscription in order to access that channel"""
        return self.http.get_discord_gold_invite()

    def get_release(self, catalog_id: str):
        """Returns a release with the given ID. If not found, raises connect.errors.NotFound."""
        return Release(**self.http.get_release(catalog_id))

    def get_track(self, track_id: str):
        """Returns a track with the given ID. If not found, raises connect.errors.NotFound."""
        return Track(**self.http.get_track(track_id))

    def get_artist(self, artist_id: str):
        """Returns a artist with the given ID. If not found, raises connect.errors.NotFound."""
        return Artist(**self.http.get_artist(artist_id))

    def get_playlist(self, playlist_id: str):
        """Returns a playlist with the given ID. If not found, raises connect.errors.NotFound."""
        return Playlist(**self.http.get_playlist(playlist_id))

    def get_all_releases(self):
        """Retrieves every release the client can 'access'"""
        releases = []
        for release in self.http.get_release_list()['results']:
            releases.append(Release(**release))
        return releases

    def get_all_tracks(self):
        """Retrieves every track the client can 'access'"""
        tracks = []
        for track in self.http.get_track_list()['results']:
            tracks.append(Track(**track))
        return tracks

    def get_all_artists(self):
        """Retrieves every artist the client can 'access'"""
        artists = []
        for artist in self.http.get_artist_list()['results']:
            artists.append(Artist(**artist))
        return artists

    def get_all_playlists(self):
        """Retrieves every playlist the client can access. If not signed it, raises connect.errors.Unauthorized."""
        playlists = []
        for playlist in self.http.get_playlist_list()['results']:
            playlists.append(Playlist(**playlist))
        return playlists

    def search_release(self, term: str, limit=None, skip=None):
        """Searches for a release. If not found, raises connect.errors.NotFound"""
        releases = []
        query = '?fuzzyOr=title,{1},renderedArtists,{1}&limit={2}&skip{3}'.format(self, quote(term), limit, skip)
        for release in self.http.get(self.http.RELEASE + query)['results']:
            releases.append(Release(**release))
        if not releases:
            raise NotFound('No release was found.')
        else:
            return releases

    def search_release_advanced(self, title: str, artists: str, limit=None, skip=None):
        """Searches for a release. If not found, raises connect.errors.NotFound"""
        releases = []
        query = '?fuzzy=title,{1},renderedArtists,{2}&limit={3}&skip{4}'.format(self, quote(title), quote(artists), limit, skip)
        for release in self.http.get(self.http.RELEASE + query)['results']:
            releases.append(Release(**release))
        if not releases:
            raise NotFound('No release was found.')
        else:
            return releases

    def search_track(self, term: str, limit=None, skip=None):
        """Searches for a track. If not found, raises connect.errors.NotFound"""
        tracks = []
        query = '?fuzzyOr=title,{1},artistsTitle,{1}&limit={2}&skip{3}'.format(self, quote(term), limit, skip)
        for track in self.http.get(self.http.TRACK + query)['results']:
            tracks.append(Track(**track))
        if not tracks:
            raise NotFound('No track was found.')
        else:
            return tracks

    def search_track_advanced(self, title: str, artists: str, limit=None, skip=None):
        """Searches for a track. If not found, raises connect.errors.NotFound"""
        tracks = []
        query = '?fuzzy=title,{1},artistsTitle,{2}&limit={3}&skip{4}'.format(self, quote(title), quote(artists), limit, skip)
        for track in self.http.get(self.http.TRACK + query)['results']:
            tracks.append(Track(**track))
        if not tracks:
            raise NotFound('No track was found.')
        else:
            return tracks

    def search_artist(self, term: str, limit=None, skip=None):
        """Searches for an artist. If not found, raises connect.errors.NotFound"""
        artists = []
        query = '?fuzzyOr=name,{1}&limit={2}&skip{3}'.format(self, quote(term), limit, skip)
        for artist in self.http.get(self.http.ARTIST + query)['results']:
            artists.append(Artist(**artist))
        if not artists:
            raise NotFound('No artist was found.')
        else:
            return artists

    def search_playlist(self, term: str, limit=None, skip=None):
        """Searches for a playlist. If not found, raises connect.errors.NotFound and if not signed it, raises connect.errors.Unauthorized."""
        playlists = []
        query = '?fuzzyOr=name,{1}&limit={2}&skip{3}'.format(self, quote(term), limit, skip)
        for playlist in self.http.get(self.http.PLAYLIST + query)['results']:
            playlists.append(Playlist(**playlist))
        if not playlists:
            raise NotFound('No playlist was found.')
        else:
            return playlists
