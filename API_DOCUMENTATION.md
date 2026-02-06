# API Documentation - Smart Mood-Based Music Suggestion System

## Overview
This document provides detailed information about all API endpoints available in the application.

## Base URL
```
http://localhost:8000
```

## Authentication
All endpoints (except login/signup) require user authentication. The application uses Django's session-based authentication.

---

## User Authentication Endpoints

### 1. User Registration (Sign Up)

**Endpoint**: `/signup/`  
**Method**: `POST`  
**Authentication**: Not required  
**Content-Type**: `application/x-www-form-urlencoded`

**Parameters**:
```json
{
    "username": "string",           // Required, unique
    "email": "string",               // Required, valid email
    "password1": "string",          // Required, min 8 chars
    "password2": "string",          // Required, must match password1
    "first_name": "string",         // Optional
    "last_name": "string"           // Optional
}
```

**Response**:
- **Success (201)**: Redirects to language selection page
- **Error (400)**: Returns form with validation errors

**Example**:
```bash
curl -X POST http://localhost:8000/signup/ \
  -d "username=john&email=john@example.com&password1=SecurePass123&password2=SecurePass123"
```

---

### 2. User Login

**Endpoint**: `/login/`  
**Method**: `POST`  
**Authentication**: Not required  
**Content-Type**: `application/x-www-form-urlencoded`

**Parameters**:
```json
{
    "username": "string",    // Required
    "password": "string"     // Required
}
```

**Response**:
- **Success (302)**: Redirects to home page, sets session cookie
- **Error (400)**: Returns login page with error message

**Example**:
```bash
curl -X POST http://localhost:8000/login/ \
  -d "username=john&password=SecurePass123" \
  -c cookies.txt
```

---

### 3. User Logout

**Endpoint**: `/logout/`  
**Method**: `GET`  
**Authentication**: Required  

**Response**:
- **Success (302)**: Redirects to landing page, clears session

**Example**:
```bash
curl http://localhost:8000/logout/ -b cookies.txt
```

---

## Page Navigation Endpoints

### 4. Landing Page

**Endpoint**: `/`  
**Method**: `GET`  
**Authentication**: Not required  
**Returns**: HTML landing page

---

### 5. Home Dashboard

**Endpoint**: `/home/`  
**Method**: `GET`  
**Authentication**: Required  
**Returns**: HTML home page with navigation options

---

### 6. Language Selection

**Endpoint**: `/language-selection/`  
**Method**: `GET, POST`  
**Authentication**: Required  

**POST Parameters**:
```json
{
    "preferred_language": "en|es|fr|de|hi|ja"  // Required
}
```

**Response**:
- **GET**: HTML form for language selection
- **POST Success**: Redirects to home page
- **POST Error**: Returns form with errors

---

### 7. Emotion Detection Page

**Endpoint**: `/emotion-detection/`  
**Method**: `GET`  
**Authentication**: Required  
**Returns**: HTML page with webcam interface

---

### 8. Playlist History

**Endpoint**: `/playlist-history/`  
**Method**: `GET`  
**Authentication**: Required  
**Returns**: HTML page with user's song history

---

### 9. User Dashboard

**Endpoint**: `/dashboard/`  
**Method**: `GET`  
**Authentication**: Required  
**Returns**: HTML page with statistics and mood charts

---

## API Endpoints (JSON)

### 10. Detect Emotion

**Endpoint**: `/api/detect-emotion/`  
**Method**: `POST`  
**Authentication**: Required  
**Content-Type**: `application/json`

**Request Body**:
```json
{
    "image": "data:image/jpeg;base64,iVBORw0KGgo..."  // Base64 encoded image
}
```

**Response Success (200)**:
```json
{
    "emotion": "happy",
    "mood": "happy",
    "confidence": 0.85
}
```

**Response Error (400)**:
```json
{
    "error": "No face detected in the image",
    "emotion": null,
    "mood": "calm"
}
```

**Possible Emotions**: `angry`, `disgust`, `fear`, `happy`, `neutral`, `sad`, `surprise`

**Possible Moods**: `angry`, `stressed`, `calm`, `happy`, `sad`, `relaxed`, `energetic`, `neutral`

**Example**:
```javascript
const canvas = document.querySelector('canvas');
const imageData = canvas.toDataURL('image/jpeg');

fetch('/api/detect-emotion/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({ image: imageData })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

### 11. Get Song Recommendations

**Endpoint**: `/api/get-songs/`  
**Method**: `POST`  
**Authentication**: Required  
**Content-Type**: `application/json`

**Request Body**:
```json
{
    "mood": "happy|sad|calm|energetic|stressed|relaxed|angry|neutral",
    "language": "en|es|fr|de|hi|ja"  // Optional, defaults to user's preference
}
```

**Response Success (200)**:
```json
{
    "songs": [
        {
            "id": 1,
            "youtube_id": "dQw4w9WgXcQ",
            "title": "Never Gonna Give You Up",
            "artist": "Rick Astley",
            "thumbnail_url": "https://i.ytimg.com/vi/...",
            "mood": "happy"
        },
        // ... more songs
    ]
}
```

**Response Error (500)**:
```json
{
    "error": "Error message describing what went wrong"
}
```

**Notes**:
- Returns up to 12 songs per request
- Fetches from YouTube API if not in local database
- Caches results in database for faster retrieval
- Results are filtered by mood and language

**Example**:
```javascript
fetch('/api/get-songs/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({
        mood: 'happy',
        language: 'en'
    })
})
.then(response => response.json())
.then(data => displaySongs(data.songs));
```

---

### 12. Play Song (Log History)

**Endpoint**: `/api/play-song/`  
**Method**: `POST`  
**Authentication**: Required  
**Content-Type**: `application/json`

**Request Body**:
```json
{
    "song_id": 1,           // Integer, database song ID
    "emotion": "happy"      // String, detected emotion
}
```

**Response Success (200)**:
```json
{
    "success": true,
    "message": "Song added to history"
}
```

**Response Error (404)**:
```json
{
    "error": "Song not found"
}
```

**Response Error (500)**:
```json
{
    "error": "Error message"
}
```

**Notes**:
- Creates a PlaylistHistory record
- Tracks user's listening patterns
- Used for dashboard statistics

**Example**:
```javascript
fetch('/api/play-song/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({
        song_id: 1,
        emotion: 'happy'
    })
})
.then(response => response.json())
.then(data => console.log(data.message));
```

---

## Error Handling

### Common HTTP Status Codes

| Code | Meaning | Common Cause |
|------|---------|------------|
| 200 | OK | Request successful |
| 302 | Redirect | Authentication required or form submitted |
| 400 | Bad Request | Invalid data or missing required fields |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Unexpected server error |

### Error Response Format

**JSON Errors**:
```json
{
    "error": "Detailed error message"
}
```

**HTML Errors**:
Redirects to error page or returns form with error messages

---

## Authentication & Security

### Session Cookies
All authenticated endpoints use Django session cookies. Cookies are:
- **Secure**: HTTPS-only in production
- **HttpOnly**: Not accessible from JavaScript
- **SameSite**: Set to "Lax" for CSRF protection

### CSRF Protection
All POST requests require a CSRF token in the `X-CSRFToken` header or as a form field.

**Getting CSRF Token**:
```javascript
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
```

**In JavaScript Fetch**:
```javascript
headers: {
    'X-CSRFToken': csrfToken
}
```

---

## Rate Limiting

Currently no rate limiting implemented. In production:
- Implement rate limiting per user
- Limit API calls to prevent abuse
- Monitor YouTube API quota

---

## Data Models

### User Model
```json
{
    "id": 1,
    "username": "john",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

### Song Model
```json
{
    "id": 1,
    "title": "Song Title",
    "artist": "Artist Name",
    "youtube_id": "dQw4w9WgXcQ",
    "mood": "happy",
    "language": "en",
    "description": "Optional description",
    "thumbnail_url": "https://...",
    "created_at": "2026-02-05T10:30:00Z"
}
```

### PlaylistHistory Model
```json
{
    "id": 1,
    "user_id": 1,
    "song_id": 1,
    "emotion_detected": "happy",
    "played_at": "2026-02-05T10:35:00Z"
}
```

---

## Supported Languages

| Code | Language |
|------|----------|
| en | English |
| es | Spanish |
| fr | French |
| de | German |
| hi | Hindi |
| ja | Japanese |

---

## Supported Moods

| Mood | Description |
|------|------------|
| happy | Uplifting, positive music |
| sad | Emotional, melancholic music |
| calm | Relaxing, peaceful music |
| energetic | Motivational, upbeat music |
| stressed | Stress relief, soothing music |
| relaxed | Chill, ambient music |
| angry | Intense, powerful music |
| neutral | General background music |

---

## Example Workflow

```
1. User accesses http://localhost:8000
2. Views landing page
3. Clicks "Sign Up"
4. Submits registration form (POST /signup/)
5. Redirected to language selection
6. Selects language (POST /language-selection/)
7. Redirected to home page
8. Clicks "Detect Your Mood"
9. Allows camera access
10. Captures emotion (POST /api/detect-emotion/)
11. Receives detected emotion
12. Requests songs (POST /api/get-songs/)
13. Receives song list
14. Clicks play button
15. Logs song play (POST /api/play-song/)
16. YouTube player displays and auto-plays
```

---

## Testing Endpoints

### Using cURL

**Test Login**:
```bash
curl -X POST http://localhost:8000/login/ \
  -d "username=john&password=SecurePass123" \
  -c cookies.txt
```

**Test Get Songs** (with session):
```bash
curl -X POST http://localhost:8000/api/get-songs/ \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: YOUR_CSRF_TOKEN" \
  -b cookies.txt \
  -d '{"mood":"happy","language":"en"}'
```

### Using Postman

1. Create collection "MoodMusic API"
2. Set base URL: `http://localhost:8000`
3. Use "Cookie" tab to manage session
4. Add CSRF token to headers

---

## Pagination

Currently no pagination implemented. In production:
- Implement pagination for large result sets
- Add `page` and `limit` parameters
- Return pagination metadata

---

## API Version

- **Current Version**: 1.0.0
- **Created**: February 5, 2026
- **Status**: Active Development

---

## Support

For API issues or questions:
1. Check error messages and HTTP status codes
2. Review request/response examples above
3. Check server logs: `tail -f /var/log/django.log`
4. Enable Django debug toolbar in development

---

**Last Updated**: February 5, 2026
