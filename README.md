# Smart Mood-Based Music Suggestion System

A Django-based web application that detects user emotions using facial recognition and recommends music based on their current mood.

## Features

- **User Authentication**: Secure login and registration system
- **Emotion Detection**: Real-time facial emotion recognition using webcam
- **Music Recommendations**: AI-powered song suggestions based on detected emotion
- **Multi-Language Support**: Support for multiple languages (English, Spanish, French, German, Hindi, Japanese)
- **Playlist History**: Track listening history and emotions
- **User Dashboard**: View statistics and mood distribution
- **YouTube Integration**: Stream songs directly from YouTube

## Project Structure

```
music_proj/
├── music_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── music_app/              # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   ├── urls.py            # URL routing
│   ├── emotion_detector.py # Emotion detection logic
│   ├── youtube_api.py     # YouTube API integration
│   ├── admin.py           # Django admin configuration
│   ├── apps.py
│   └── signals.py
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── landing.html       # Landing page
│   ├── login.html         # Login page
│   ├── signup.html        # Signup page
│   ├── language_selection.html
│   ├── home.html          # Home page
│   ├── emotion_detection.html
│   ├── playlist_history.html
│   └── dashboard.html
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploaded files
├── manage.py
├── requirements.txt       # Python dependencies
└── README.md
```

## Installation

### Prerequisites
- Python 3.8+
- MySQL Server
- Git

### Setup Steps

1. **Clone the repository**
```bash
cd e:\new_music_proj
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure database**
Edit `music_project/settings.py` and update MySQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_suggestion_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

5. **Get YouTube API Key**
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project
- Enable YouTube Data API v3
- Create API key
- Update `YOUTUBE_API_KEY` in `music_project/settings.py`

6. **Create database**
```bash
mysql -u root -p
CREATE DATABASE music_suggestion_db;
exit
```

7. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

8. **Create superuser**
```bash
python manage.py createsuperuser
```

9. **Collect static files**
```bash
python manage.py collectstatic
```

10. **Run development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Usage

1. **Register/Login**: Create an account or login
2. **Select Language**: Choose your preferred language
3. **Detect Emotion**: 
   - Click "Detect Your Mood"
   - Allow camera access
   - Click "Start Camera"
   - Position your face and click "Capture Emotion"
4. **Get Recommendations**: Browse recommended songs for your mood
5. **Play Songs**: Click play to listen to a song
6. **View History**: Check your listening history and mood statistics

## API Endpoints

- `POST /api/detect-emotion/` - Detect emotion from image
- `POST /api/get-songs/` - Get song recommendations
- `POST /api/play-song/` - Log song play action

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: MySQL
- **AI/ML**: TensorFlow, OpenCV
- **APIs**: YouTube Data API v3
- **Additional**: Django REST Framework, CORS Headers

## Models

### UserProfile
- User information and language preference
- Profile picture storage

### Song
- Song details (title, artist, YouTube ID)
- Mood classification
- Language categorization

### PlaylistHistory
- Track user's song plays
- Record detected emotions
- Timestamp logging

### UserPreferences
- Favorite moods and artists
- User customization options

## Configuration Notes

1. **Emotion Detection**: Uses a pre-trained TensorFlow model
2. **YouTube API**: Limited quota, ensure you have sufficient API calls
3. **Database**: Configure MySQL credentials in settings.py
4. **CORS**: Update `ALLOWED_HOSTS` for production use

## Future Enhancements

- Real-time music streaming
- Social features (share playlists)
- Advanced emotion analysis
- Mobile app version
- Spotify integration
- Machine learning model improvements
- Recommendation algorithm enhancement

## Troubleshooting

### Camera not working
- Check browser permissions
- Ensure HTTPS in production
- Test with a different browser

### No face detected
- Ensure proper lighting
- Position face clearly in frame
- Check camera resolution

### YouTube API errors
- Verify API key is valid
- Check API quota
- Ensure API is enabled in Google Cloud

## License

This project is for educational purposes.

## Support

For issues or questions, please refer to the documentation or contact the development team.
