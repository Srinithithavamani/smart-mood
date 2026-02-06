# 🚀 SETUP INSTRUCTIONS - NEXT STEPS

## ✅ What We Just Fixed
- Installed all required Django packages
- Django configuration verified ✓
- Ready to run the application

## ⚠️ BEFORE YOU RUN THE APP

### Step 1: Create MySQL Database

1. **Start MySQL** (if not already running)
   - Open MySQL Command Line Client
   - Or use MySQL Workbench

2. **Create the database**
   ```sql
   CREATE DATABASE music_suggestion_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

### Step 2: Update Django Settings

Edit `music_project/settings.py` and find the DATABASES section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_suggestion_db',      # Database name
        'USER': 'root',                      # MySQL username
        'PASSWORD': 'your_password',         # ← UPDATE THIS (your MySQL password)
        'HOST': '127.0.0.1',                 # MySQL host
        'PORT': '3306',                      # MySQL port
    }
}
```

### Step 3: Add YouTube API Key (Optional)

In `music_project/settings.py`, find and update:

```python
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'  # ← Get from Google Cloud Console
```

### Step 4: Run Database Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin Account

```powershell
python manage.py createsuperuser
```
Follow the prompts to create username, email, and password.

### Step 6: Collect Static Files

```powershell
python manage.py collectstatic --noinput
```

### Step 7: Start the Server

```powershell
python manage.py runserver
```

Then visit: **http://localhost:8000**

---

## 📝 IMPORTANT NOTES

### About Emotion Detection
- The emotion detection feature uses TensorFlow
- For now, it will work with a fallback neutral emotion
- To enable full emotion detection, place the `emotion_model.h5` file in `music_app/models/`
- You can train your own model or download a pre-trained one

### About YouTube API
- YouTube music search will work WITHOUT an API key (uses public data)
- With an API key, you get more results and better performance
- Get a free API key from: https://console.cloud.google.com/

### Database
- Uses MySQL (required)
- SQLite can work for testing, but MySQL is recommended
- Make sure MySQL is running before running migrations

---

## 🔧 TROUBLESHOOTING

### Error: "Can't connect to MySQL server"
- Make sure MySQL is running
- Check your MySQL credentials are correct in settings.py
- Verify the database exists

### Error: "No module named 'corsheaders'"
- Run: `pip install -r requirements.txt`

### Error: "Static files not found"
- Run: `python manage.py collectstatic --noinput`

### Emotion detection not working
- This is optional - the app works fine without it
- Add TensorFlow when you're ready: `pip install tensorflow`

---

## ✨ QUICK REFERENCE

### Essential Commands
```powershell
# Check Django configuration
python manage.py check

# Create database migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create admin account
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Start development server
python manage.py runserver

# Access admin panel
# Visit: http://localhost:8000/admin
```

### File Locations to Edit
| File | What to Change |
|------|---|
| `music_project/settings.py` | MySQL credentials, YouTube API key |
| `music_app/models.py` | Database models (if customizing) |
| `templates/` | HTML templates (if customizing) |
| `static/css/style.css` | Styling (if customizing) |

---

## 📚 NEXT: Follow These Steps

1. ✅ Packages installed (DONE)
2. ⏳ Create MySQL database (NEXT)
3. ⏳ Update Django settings
4. ⏳ Run migrations
5. ⏳ Create superuser
6. ⏳ Start server
7. ⏳ Access at http://localhost:8000

---

**Let me know when you've:**
1. Created the MySQL database
2. Updated the settings.py file with your MySQL password
3. Then I can help with the migrations!
