import unittest

from lyrics import lyrics_find

class TestLyrics(unittest.TestCase):
    def test_lyrics_good_request(self):
        """
        Get Lyrics With Artist Name and Song Title - 200
        """
        Artist = 'Sia'
        Song = 'Together'
        result = lyrics_find(Artist, Song)
        return self.assertEqual(result, 200)
        
    def test_lyrics_bad_request(self):
        """
        Get Lyrics With Artist Name and Song Title - 404 Error
        """
        Artist = 'No Artist With This Name'
        Song = 'No Song With This Name'
        result = lyrics_find(Artist, Song)
        return(self.assertEqual(result, 404) or self.assertEqual(result, 403))

if __name__ == '__main__':
    unittest.main()