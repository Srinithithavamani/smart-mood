"""
Tests for music_app
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile, Song, PlaylistHistory


class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_signup_page_loads(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_user_signup(self):
        response = self.client.post('/signup/', {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!'
        })
        self.assertTrue(User.objects.filter(username='testuser').exists())
    
    def test_user_login(self):
        User.objects.create_user(username='testuser', password='TestPass123!')
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'TestPass123!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login


class UserProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPass123!')
        self.profile = UserProfile.objects.get(user=self.user)
    
    def test_user_profile_created(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.preferred_language, 'en')
    
    def test_language_preference_update(self):
        self.profile.preferred_language = 'es'
        self.profile.save()
        self.assertEqual(self.profile.preferred_language, 'es')


class SongTests(TestCase):
    def setUp(self):
        self.song = Song.objects.create(
            title='Test Song',
            artist='Test Artist',
            youtube_id='dQw4w9WgXcQ',
            mood='happy',
            language='en'
        )
    
    def test_song_creation(self):
        self.assertEqual(self.song.title, 'Test Song')
        self.assertEqual(self.song.mood, 'happy')
    
    def test_song_mood_filtering(self):
        songs = Song.objects.filter(mood='happy')
        self.assertEqual(songs.count(), 1)
