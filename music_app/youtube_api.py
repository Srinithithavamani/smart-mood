import requests
from django.conf import settings


# Fallback music data for when YouTube API is unavailable
FALLBACK_SONGS = {
    'happy': [
        {'youtube_id': '3JZ4pnNtyxQ', 'title': 'Happy Upbeat', 'artist': 'Sample Artist A', 'thumbnail_url': 'https://i.ytimg.com/vi/3JZ4pnNtyxQ/mqdefault.jpg', 'mood': 'happy', 'language': 'en'},
        {'youtube_id': 'LsoLEjrDogU', 'title': 'Joyful Tune', 'artist': 'Sample Artist B', 'thumbnail_url': 'https://i.ytimg.com/vi/LsoLEjrDogU/mqdefault.jpg', 'mood': 'happy', 'language': 'en'},
        {'youtube_id': '60ItHLz5WEA', 'title': 'Sunny Days', 'artist': 'Sample Artist C', 'thumbnail_url': 'https://i.ytimg.com/vi/60ItHLz5WEA/mqdefault.jpg', 'mood': 'happy', 'language': 'en'},
        {'youtube_id': 'kXYiU_JCYtU', 'title': 'Optimistic Beat', 'artist': 'Sample Artist D', 'thumbnail_url': 'https://i.ytimg.com/vi/kXYiU_JCYtU/mqdefault.jpg', 'mood': 'happy', 'language': 'en'},
        {'youtube_id': 'fJ9rUzIMcZQ', 'title': 'Feel Good Song', 'artist': 'Sample Artist E', 'thumbnail_url': 'https://i.ytimg.com/vi/fJ9rUzIMcZQ/mqdefault.jpg', 'mood': 'happy', 'language': 'en'},
    ],
    'sad': [
        {'youtube_id': 'hLQl3WQQoQ0', 'title': 'Melancholy Piano', 'artist': 'Sample Artist F', 'thumbnail_url': 'https://i.ytimg.com/vi/hLQl3WQQoQ0/mqdefault.jpg', 'mood': 'sad', 'language': 'en'},
        {'youtube_id': 'kVpv8-5XWOI', 'title': 'Sad Strings', 'artist': 'Sample Artist G', 'thumbnail_url': 'https://i.ytimg.com/vi/kVpv8-5XWOI/mqdefault.jpg', 'mood': 'sad', 'language': 'en'},
        {'youtube_id': 'hT_nvWreIhg', 'title': 'Lonely Sound', 'artist': 'Sample Artist H', 'thumbnail_url': 'https://i.ytimg.com/vi/hT_nvWreIhg/mqdefault.jpg', 'mood': 'sad', 'language': 'en'},
        {'youtube_id': '04854XqcfCY', 'title': 'Tearful Melody', 'artist': 'Sample Artist I', 'thumbnail_url': 'https://i.ytimg.com/vi/04854XqcfCY/mqdefault.jpg', 'mood': 'sad', 'language': 'en'},
        {'youtube_id': 'CevxZvSJLk8', 'title': 'Blue Notes', 'artist': 'Sample Artist J', 'thumbnail_url': 'https://i.ytimg.com/vi/CevxZvSJLk8/mqdefault.jpg', 'mood': 'sad', 'language': 'en'},
    ],
    'fear': [
        {'youtube_id': '2vjPBrBU-TM', 'title': 'Tense Atmosphere', 'artist': 'Sample Artist K', 'thumbnail_url': 'https://i.ytimg.com/vi/2vjPBrBU-TM/mqdefault.jpg', 'mood': 'fear', 'language': 'en'},
        {'youtube_id': 'RgKAFK5djSk', 'title': 'Eerie Sounds', 'artist': 'Sample Artist L', 'thumbnail_url': 'https://i.ytimg.com/vi/RgKAFK5djSk/mqdefault.jpg', 'mood': 'fear', 'language': 'en'},
        {'youtube_id': 'uelHwf8o7_U', 'title': 'Dark Ambience', 'artist': 'Sample Artist M', 'thumbnail_url': 'https://i.ytimg.com/vi/uelHwf8o7_U/mqdefault.jpg', 'mood': 'fear', 'language': 'en'},
        {'youtube_id': 'pRpeEdMmmQ0', 'title': 'Creepy Tone', 'artist': 'Sample Artist N', 'thumbnail_url': 'https://i.ytimg.com/vi/pRpeEdMmmQ0/mqdefault.jpg', 'mood': 'fear', 'language': 'en'},
        {'youtube_id': 'kXYiU_JCYtU', 'title': 'Subtle Horror', 'artist': 'Sample Artist O', 'thumbnail_url': 'https://i.ytimg.com/vi/kXYiU_JCYtU/mqdefault.jpg', 'mood': 'fear', 'language': 'en'},
    ],
    'surprise': [
        {'youtube_id': 'dQw4w9WgXcQ', 'title': 'Upbeat Surprise', 'artist': 'Sample Artist P', 'thumbnail_url': 'https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg', 'mood': 'surprise', 'language': 'en'},
        {'youtube_id': 'VbfpW0pbvaU', 'title': 'Unexpected Drop', 'artist': 'Sample Artist Q', 'thumbnail_url': 'https://i.ytimg.com/vi/VbfpW0pbvaU/mqdefault.jpg', 'mood': 'surprise', 'language': 'en'},
        {'youtube_id': 'fJ9rUzIMcZQ', 'title': 'Big Reveal', 'artist': 'Sample Artist R', 'thumbnail_url': 'https://i.ytimg.com/vi/fJ9rUzIMcZQ/mqdefault.jpg', 'mood': 'surprise', 'language': 'en'},
        {'youtube_id': '3JZ4pnNtyxQ', 'title': 'Sudden Energy', 'artist': 'Sample Artist S', 'thumbnail_url': 'https://i.ytimg.com/vi/3JZ4pnNtyxQ/mqdefault.jpg', 'mood': 'surprise', 'language': 'en'},
        {'youtube_id': '60ItHLz5WEA', 'title': 'Exciting Beat', 'artist': 'Sample Artist T', 'thumbnail_url': 'https://i.ytimg.com/vi/60ItHLz5WEA/mqdefault.jpg', 'mood': 'surprise', 'language': 'en'},
    ],
    'disgust': [
        {'youtube_id': 'kJQP7kiw9l0', 'title': 'Intense Music', 'artist': 'Sample Artist U', 'thumbnail_url': 'https://i.ytimg.com/vi/kJQP7kiw9l0/mqdefault.jpg', 'mood': 'disgust', 'language': 'en'},
        {'youtube_id': '9bZkp7q19f0', 'title': 'Aggressive Theme', 'artist': 'Sample Artist V', 'thumbnail_url': 'https://i.ytimg.com/vi/9bZkp7q19f0/mqdefault.jpg', 'mood': 'disgust', 'language': 'en'},
        {'youtube_id': 'OPf0YbXqDm0', 'title': 'Harsh Rhythm', 'artist': 'Sample Artist W', 'thumbnail_url': 'https://i.ytimg.com/vi/OPf0YbXqDm0/mqdefault.jpg', 'mood': 'disgust', 'language': 'en'},
        {'youtube_id': 'hLQl3WQQoQ0', 'title': 'Bruising Sound', 'artist': 'Sample Artist X', 'thumbnail_url': 'https://i.ytimg.com/vi/hLQl3WQQoQ0/mqdefault.jpg', 'mood': 'disgust', 'language': 'en'},
        {'youtube_id': 'kVpv8-5XWOI', 'title': 'Dark Power', 'artist': 'Sample Artist Y', 'thumbnail_url': 'https://i.ytimg.com/vi/kVpv8-5XWOI/mqdefault.jpg', 'mood': 'disgust', 'language': 'en'},
    ],
    'neutral': [
        {'youtube_id': '2WPCLsHt-1w', 'title': 'Background Music', 'artist': 'Ambient Music', 'thumbnail_url': 'https://i.ytimg.com/vi/2WPCLsHt-1w/mqdefault.jpg', 'mood': 'neutral', 'language': 'en'},
        {'youtube_id': '5qap5aO4i9A', 'title': 'Lo-fi Beat', 'artist': 'Sample Artist Z', 'thumbnail_url': 'https://i.ytimg.com/vi/5qap5aO4i9A/mqdefault.jpg', 'mood': 'neutral', 'language': 'en'},
        {'youtube_id': 'DWcJFNfaw9c', 'title': 'Calm Instrumental', 'artist': 'Sample Artist AA', 'thumbnail_url': 'https://i.ytimg.com/vi/DWcJFNfaw9c/mqdefault.jpg', 'mood': 'neutral', 'language': 'en'},
        {'youtube_id': '7wtfhZwyrcc', 'title': 'Ambient Space', 'artist': 'Sample Artist AB', 'thumbnail_url': 'https://i.ytimg.com/vi/7wtfhZwyrcc/mqdefault.jpg', 'mood': 'neutral', 'language': 'en'},
        {'youtube_id': 'kXYiU_JCYtU', 'title': 'Soft Background', 'artist': 'Sample Artist AC', 'thumbnail_url': 'https://i.ytimg.com/vi/kXYiU_JCYtU/mqdefault.jpg', 'mood': 'neutral', 'language': 'en'},
    ]
}


class YouTubeAPI:
    def __init__(self):
        self.api_key = settings.YOUTUBE_API_KEY
        self.base_url = 'https://www.googleapis.com/youtube/v3'
    
    def search_songs_by_mood_and_language(self, mood, language='en'):
        """
        Search for songs based on mood and language
        Returns: List of songs with YouTube IDs
        """
        try:
            # Map mood to search keywords
            mood_keywords = {
                'happy': 'happy uplifting music',
                'sad': 'sad emotional music',
                'fear': 'calm relaxing music',
                'surprise': 'energetic music',
                'disgust': 'intense powerful music',
                'neutral': 'background music instrumental'
            }
            
            # Map language to search terms
            language_keywords = {
                'en': 'English',
                'es': 'Spanish',
                'fr': 'French',
                'de': 'German',
                'hi': 'Hindi',
                'ja': 'Japanese',
                'ta': 'Tamil',
                'te': 'Telugu',
                'ml': 'Malayalam',
                'kn': 'Kannada'
            }
            
            query = f"{mood_keywords.get(mood, 'music')} {language_keywords.get(language, '')} songs"
            
            params = {
                'part': 'snippet',
                'q': query,
                'type': 'video',
                'maxResults': 12,
                'key': self.api_key,
                'order': 'relevance'
            }
            
            response = requests.get(f"{self.base_url}/search", params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            songs = []
            
            for item in data.get('items', []):
                song_info = {
                    'youtube_id': item['id'].get('videoId'),
                    'title': item['snippet'].get('title'),
                    'artist': item['snippet'].get('channelTitle'),
                    'thumbnail_url': item['snippet']['thumbnails']['medium'].get('url'),
                    'mood': mood,
                    'language': language
                }
                songs.append(song_info)
            
            return songs
        
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                print(f"YouTube API 403 Forbidden - Using fallback songs. Make sure YouTube Data API v3 is enabled in your Google Cloud Console")
            else:
                print(f"HTTP Error searching YouTube: {e}")
            return self._get_fallback_songs(mood, language)
        
        except Exception as e:
            print(f"Error searching YouTube: {e}. Using fallback songs.")
            return self._get_fallback_songs(mood, language)
    
    def _get_fallback_songs(self, mood, language='en'):
        """Return fallback songs when API is unavailable"""
        return FALLBACK_SONGS.get(mood, [])
    
    def get_video_details(self, video_id):
        """
        Get detailed information about a video
        Returns: Video details dictionary
        """
        try:
            params = {
                'part': 'snippet,contentDetails',
                'id': video_id,
                'key': self.api_key
            }
            
            response = requests.get(f"{self.base_url}/videos", params=params)
            response.raise_for_status()
            
            data = response.json()
            if data.get('items'):
                item = data['items'][0]
                return {
                    'title': item['snippet'].get('title'),
                    'description': item['snippet'].get('description'),
                    'duration': item['contentDetails'].get('duration'),
                    'thumbnail_url': item['snippet']['thumbnails']['high'].get('url')
                }
            
            return None
        
        except Exception as e:
            print(f"Error getting video details: {e}")
            return None
