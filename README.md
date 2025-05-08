# Brainwaze Learning App

🚀 A next-generation learning platform (currently in early development)

## Current Features (v0.1)

### Authentication System
- **User Registration**
  - Student/Instructor role selection
  - Email and username validation
  - Secure password handling

- **JWT Authentication**
  - Secure login/logout
  - Token refresh functionality
  - Protected endpoints

- **Profile Management**
  - Basic user profiles (basic, profile picture)
  - Student-specific profiles 
  - Instructor-specific profiles 

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.2+

### Installation
```bash
git clone https://github.com/brainwaze/learning-app.git
cd learning-app
pip install -r requirements.txt
python manage.py migrate
```

### Running the Server
```bash
python manage.py runserver
```

## API Documentation

### Authentication Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/register/` | POST | Register new user |
| `/auth/login/` | POST | Login with credentials |
| `/auth/token/refresh/` | POST | Refresh JWT token |

### Profile Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/profile/` | GET | View user profile |
| `/auth/profile/update/` | PATCH | Update profile |
| `/auth/profile/student/` | PATCH | Update student profile |
| `/auth/profile/instructor/` | PATCH | Update instructor profile |

## Coming Soon
- Course management system
- Learning progress tracking
- Interactive content features

## Development Roadmap
- [x] Phase 1: Authentication & Profiles (Current)
- [ ] Phase 2: Course Management
- [ ] Phase 3: Learning Analytics
- [ ] Phase 4: Mobile Integration

---

*Brainwaze - Redefining learning experiences*  
[Website Coming Soon] | contact@brainwaze.com
```
