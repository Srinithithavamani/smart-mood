# Configuration Guide for Smart Mood-Based Music Suggestion System

## Table of Contents
1. [Database Setup](#database-setup)
2. [YouTube API Configuration](#youtube-api-configuration)
3. [Environment Variables](#environment-variables)
4. [Django Settings](#django-settings)
5. [Emotion Detection Model](#emotion-detection-model)
6. [Deployment](#deployment)

## Database Setup

### MySQL Configuration

1. **Install MySQL Server**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - Follow the installation wizard

2. **Create Database**
   ```bash
   mysql -u root -p
   CREATE DATABASE music_suggestion_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   exit
   ```

3. **Update Django Settings**
   Edit `music_project/settings.py`:
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

4. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## YouTube API Configuration

### Step 1: Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project dropdown and select "NEW PROJECT"
3. Enter project name: "MoodMusic"
4. Click "CREATE"

### Step 2: Enable YouTube Data API v3
1. Go to "APIs & Services" > "Library"
2. Search for "YouTube Data API v3"
3. Click on it and press "ENABLE"

### Step 3: Create API Key
1. Go to "APIs & Services" > "Credentials"
2. Click "CREATE CREDENTIALS" > "API Key"
3. Copy the generated API key
4. Click "RESTRICT KEY"
5. Under "Application restrictions", select "HTTP referrers (web sites)"
6. Add your domain(s): `localhost`, `127.0.0.1:8000`, `yourdomain.com`
7. Under "API restrictions", select "YouTube Data API v3"

### Step 4: Update Django Settings
Edit `music_project/settings.py`:
```python
YOUTUBE_API_KEY = 'YOUR_API_KEY_HERE'
```

Or add to `.env`:
```
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```

## Environment Variables

Create a `.env` file in the project root:

```
# Django Settings
SECRET_KEY=your-secret-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=music_suggestion_db
DATABASE_USER=root
DATABASE_PASSWORD=your_password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306

# YouTube API
YOUTUBE_API_KEY=your_youtube_api_key

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:8000
```

## Django Settings

### Key Settings to Configure

1. **SECRET_KEY**
   ```python
   SECRET_KEY = 'change-this-to-a-random-string'
   ```
   Generate a new one:
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

2. **DEBUG Mode**
   ```python
   DEBUG = True  # Set to False in production
   ```

3. **ALLOWED_HOSTS**
   ```python
   ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']
   ```

4. **CORS Settings**
   ```python
   CORS_ALLOWED_ORIGINS = [
       'http://localhost:3000',
       'http://127.0.0.1:8000',
   ]
   ```

5. **Session Configuration**
   ```python
   SESSION_COOKIE_AGE = 1209600  # 2 weeks
   SESSION_COOKIE_SECURE = True  # Only in production with HTTPS
   SESSION_COOKIE_HTTPONLY = True
   ```

## Emotion Detection Model

### Model Setup

1. **Download Pre-trained Model**
   - Model should be placed in: `music_app/models/emotion_model.h5`
   - If not available, the system will use fallback neutral emotion
   - Training data: FER2013 or AffectNet dataset

2. **Model Architecture**
   - 7 emotion classes: angry, disgust, fear, happy, neutral, sad, surprise
   - Input: 48x48 grayscale images
   - Output: 7-class emotion probability

3. **Update Model Path (if needed)**
   Edit `music_app/emotion_detector.py`:
   ```python
   self.emotion_model_path = os.path.join(
       os.path.dirname(__file__), 
       'models', 
       'emotion_model.h5'
   )
   ```

## Deployment

### Production Checklist

1. **Security**
   ```python
   DEBUG = False
   SECRET_KEY = 'generate-new-secure-key'
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SESSION_COOKIE_SECURE = True
   SESSION_COOKIE_HTTPONLY = True
   SECURE_SSL_REDIRECT = True
   CSRF_COOKIE_SECURE = True
   ```

2. **Database**
   - Use managed database service (AWS RDS, Google Cloud SQL, etc.)
   - Use strong passwords
   - Enable SSL connection

3. **Static Files**
   ```bash
   python manage.py collectstatic --noinput
   # Use CDN or serve from cloud storage
   ```

4. **Media Files**
   - Store in cloud storage (AWS S3, Google Cloud Storage)
   - Update Django settings for storage backend

5. **Web Server Setup**
   ```bash
   # Using Gunicorn + Nginx
   pip install gunicorn
   gunicorn music_project.wsgi:application --bind 0.0.0.0:8000
   ```

6. **SSL/TLS Certificate**
   - Use Let's Encrypt (free)
   - Configure Nginx to use HTTPS

7. **Monitoring**
   - Set up logging
   - Monitor error rates
   - Set up alerts

### Docker Deployment (Optional)

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "music_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t moodmusic .
docker run -p 8000:8000 moodmusic
```

## Troubleshooting

### Database Connection Issues
- Verify MySQL is running
- Check credentials in settings.py
- Ensure database exists

### Camera Not Working
- Check browser permissions
- Use HTTPS in production
- Test in incognito mode

### YouTube API Quota Exceeded
- Check quota in Google Cloud Console
- Implement caching for API responses
- Consider implementing rate limiting

### Emotion Detection Not Working
- Verify model file exists
- Check image resolution
- Ensure proper lighting in webcam feed

## Support and Resources

- Django Documentation: https://docs.djangoproject.com/
- YouTube API Documentation: https://developers.google.com/youtube/v3
- OpenCV Documentation: https://docs.opencv.org/
- TensorFlow Documentation: https://www.tensorflow.org/

For more help, refer to the main README.md file.
