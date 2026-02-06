# Quick Start Guide

## Installation (Windows PowerShell)

1. **Open PowerShell and navigate to project folder**
```powershell
cd e:\new_music_proj
```

2. **Create Virtual Environment**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```
*If you get an execution policy error, run:*
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. **Install Dependencies**
```powershell
pip install -r requirements.txt
```

4. **Configure Database**
   - Open MySQL and create database:
   ```sql
   CREATE DATABASE music_suggestion_db;
   ```
   - Edit `music_project/settings.py` and update MySQL credentials

5. **Set Up YouTube API**
   - Get API key from Google Cloud Console
   - Update `YOUTUBE_API_KEY` in `music_project/settings.py`

6. **Run Migrations**
```powershell
python manage.py makemigrations
python manage.py migrate
```

7. **Create Superuser**
```powershell
python manage.py createsuperuser
```

8. **Collect Static Files**
```powershell
python manage.py collectstatic --noinput
```

9. **Run Development Server**
```powershell
python manage.py runserver
```

10. **Access the Application**
    - Main site: http://localhost:8000
    - Admin panel: http://localhost:8000/admin

## First Run

1. **Register a new account**
   - Click "Sign Up" on landing page
   - Fill in username, email, and password

2. **Select Language**
   - Choose your preferred language

3. **Test Emotion Detection**
   - Go to "Detect Your Mood"
   - Click "Start Camera"
   - Position your face clearly
   - Click "Capture Emotion"
   - Browse recommended songs

4. **Play Music**
   - Click "Play" on any song
   - Enjoy the YouTube player with autoplay

## Project Structure

```
e:\new_music_proj\
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── setup.py                  # Setup script
├── README.md                 # Project documentation
├── CONFIGURATION.md          # Configuration guide
├── QUICKSTART.md            # This file
│
├── music_project/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
│
├── music_app/               # Main application
│   ├── models.py            # Database models
│   ├── views.py             # Views/Controllers
│   ├── forms.py             # Forms
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── signals.py           # Django signals
│   ├── emotion_detector.py  # Emotion detection logic
│   ├── youtube_api.py       # YouTube API integration
│   ├── tests.py             # Tests
│   └── __init__.py
│
├── templates/               # HTML templates
│   ├── base.html
│   ├── landing.html
│   ├── login.html
│   ├── signup.html
│   ├── language_selection.html
│   ├── home.html
│   ├── emotion_detection.html
│   ├── playlist_history.html
│   └── dashboard.html
│
├── static/                  # Static files
│   └── css/
│       └── style.css
│
├── media/                   # User uploads
└── venv/                    # Virtual environment
```

## Important Files to Update

### 1. `music_project/settings.py`
Update these settings:
```python
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_suggestion_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',  # Update this
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

SECRET_KEY = 'your-secret-key'  # Generate new one for production
```

### 2. `.env` file (Optional, create from `.env.example`)
```
YOUTUBE_API_KEY=your_api_key
DATABASE_PASSWORD=your_password
```

## Common Commands

### Database Operations
```powershell
# Create migrations for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Check migration status
python manage.py showmigrations

# Revert database to previous state
python manage.py migrate music_app 0001
```

### Django Shell
```powershell
# Access Django shell to test code
python manage.py shell

# Example: Create test user
>>> from django.contrib.auth.models import User
>>> User.objects.create_user(username='test', password='test123')
```

### Running Tests
```powershell
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test music_app

# Run with verbosity
python manage.py test -v 2
```

### Static Files
```powershell
# Collect static files for production
python manage.py collectstatic

# Collect without prompting
python manage.py collectstatic --noinput
```

### Admin Operations
```powershell
# Create superuser
python manage.py createsuperuser

# Change admin password
python manage.py changepassword admin_username
```

## Features Overview

### 1. User Authentication
- Secure registration with email validation
- Login/Logout functionality
- Session management

### 2. Emotion Detection
- Real-time facial emotion recognition via webcam
- 7 emotion categories (happy, sad, angry, neutral, etc.)
- Confidence score display

### 3. Music Recommendations
- YouTube API integration
- Mood-based song suggestions
- Multi-language support
- Automatic song search

### 4. Music Player
- Embedded YouTube player
- Direct playback in application
- Song history tracking

### 5. User Dashboard
- Listening statistics
- Mood distribution charts
- Play history
- User preferences

### 6. Language Support
- English, Spanish, French, German, Hindi, Japanese
- Per-user language preference
- Language-specific recommendations

## Troubleshooting

### Virtual Environment Issues
```powershell
# Reactivate virtual environment
venv\Scripts\Activate.ps1

# Deactivate
deactivate
```

### MySQL Connection Error
1. Verify MySQL is running
2. Check credentials in settings.py
3. Ensure database exists:
   ```sql
   SHOW DATABASES;
   ```

### Migration Errors
```powershell
# Reset migrations (WARNING: deletes database)
python manage.py migrate music_app zero

# Reapply migrations
python manage.py migrate
```

### Static Files Not Loading
```powershell
# Clear and collect static files
python manage.py collectstatic --clear --noinput
```

### Camera Permission Issues
- Check browser permissions
- Try incognito mode
- Restart browser
- Allow HTTPS in production

## Next Steps

1. ✅ Basic setup complete
2. 📝 Customize email notifications
3. 🎨 Enhance UI with more themes
4. 📊 Add advanced analytics
5. 🌐 Deploy to production server
6. 📱 Create mobile app
7. 🔗 Integrate Spotify API
8. 🤖 Train custom emotion model

## Getting Help

- Read [README.md](README.md) for detailed documentation
- Check [CONFIGURATION.md](CONFIGURATION.md) for advanced setup
- Review Django docs: https://docs.djangoproject.com/
- YouTube API docs: https://developers.google.com/youtube/v3

## Security Notes

⚠️ **Before Production Deployment:**
- Change `SECRET_KEY` to a new random value
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS`
- Use HTTPS
- Store passwords securely
- Enable CSRF protection
- Set secure cookie flags

---
**Last Updated:** February 5, 2026
**Version:** 1.0.0
