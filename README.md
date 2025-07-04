# Django Session Authentication Backend

This project provides a robust session-based authentication backend using Django and Django REST Framework. It includes endpoints for user registration, login (to establish a session), logout (to invalidate a session), and a protected example endpoint that requires authentication.

---

## 🚀 Features

- **User Registration** (`/api/register/`)
- **User Login** (`/api/login/`) – Establishes a session and returns a CSRF token
- **User Logout** (`/api/logout/`) – Invalidates the session
- **Protected API Endpoint** (`/api/protected/`) – Accessible only with an active session
- **CORS Protection** for secure session management

---

## ⚙️ Setup Instructions

Follow these steps to get the Django backend up and running on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd django_session_auth_backend
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
macOS/Linux:
```bash
source venv/bin/activate
```
Windows (Command Prompt):
```bash
venv\Scripts\activate.bat
```
Windows (PowerShell):
```bash
venv\Scripts\Activate.ps1
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Configure Project Files
Ensure your project files are set up as follows:

- Allow CORS from your frontend:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```
### 6. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
### 8. Run the Development Server
```bash
python manage.py runserver
```
Backend will be available at: http://127.0.0.1:8000/

---


## 🔌 API Endpoints

All endpoints are prefixed with /api/.

### 📥 POST /api/register/
Description: Register a new user.

Request Body:
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "strongpassword123",
  "password2": "strongpassword123"
}
```
Success Response:
```json
{
  "id": 1,
  "username": "newuser",
  "email": "newuser@example.com"
}
```
##

### 🔐 POST /api/login/
Description: Authenticate user and obtain session cookie and CSRF token.

Request Body:
```json
{
  "username": "existinguser",
  "password": "theirpassword"
}
```
Success Response:
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "existinguser",
    "email": "existinguser@example.com"
  },
  "csrf_token": "your_generated_csrf_token"
}
```
##

### 🚪 POST /api/logout/
Description: Logout user and invalidate session.

Headers:
```makefile
X-CSRFToken: <your_csrf_token>
```
(Requires a valid session cookie to be sent automatically by the client)

Success Response:
```json
{
  "message": "Logout successful"
}
```
##

### 🔒 GET /api/user/
Description: Access a protected endpoint to get current user details.

Headers:
(Requires a valid session cookie to be sent automatically by the client)

Success Response:
```json
{
  "id": 1,
  "username": "logged_in_user",
  "email": "user@example.com"
}
```
Unauthorized Response:
```json
{
  "detail": "Authentication credentials were not provided."
}
```
---

## 🧪 Testing Endpoints
Use tools like curl, Postman, or Insomnia.

### Register a User
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "password123", "password2": "password123"}' \
http://127.0.0.1:8000/api/register/
```
### Login and Get Session/CSRF Token
```bash
# This command will save the session cookie to cookies.txt
curl -X POST -H "Content-Type: application/json" -c cookies.txt \
-d '{"username": "testuser", "password": "password123"}' \
http://127.0.0.1:8000/api/login/
# You'll need to manually extract the csrf_token from the JSON response for subsequent POST/PUT/DELETE requests.
```
### Access Protected Endpoint
```bash
# Use the saved session cookie
curl -X GET -b cookies.txt \
http://127.0.0.1:8000/api/user/

```
### Logout
```bash
# You need to extract the CSRF token from the login response or the browsable API.
# Example with placeholder CSRF_TOKEN:
curl -X POST -H "Content-Type: application/json" -H "X-CSRFToken: YOUR_CSRF_TOKEN_HERE" -b cookies.txt \
http://127.0.0.1:8000/api/logout/
```
##

### 📝 License
This project is open-source and free to use.

##

### 💡 Contribution
Feel free to fork the repository and submit pull requests to improve functionality or documentation.
