# Username & Password Generator API

A simple REST API built with **Python, Django, and Django REST Framework** that generates username suggestions and customizable passwords.

## Features

- Generate at least 3 username suggestions from a given name.
- Generate random passwords with customizable options.
- Choose whether to include:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Symbols (!, @, #, etc.)
- Input validation and appropriate HTTP status codes.
- JSON-based requests and responses.

## Technologies Used

- Python
- Django
- Django REST Framework

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/RahalDz-bit/generator.git
```

Navigate into the project directory:

```bash
cd YOUR_PROJECT_FOLDER
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### 1. Home

**GET** `/`

Returns a welcome message and a short API description.

### 2. Generate Username

**POST** `/username/`

Generates at least 3 username suggestions based on the provided name.

**Request Body:**

```json
{
    "name": "Akram"
}
```

**Example Response:**

```json
{
    "username1": "Akram_42",
    "username2": "15_Akram",
    "username3": "Akram_87",
    "message": "Usernames generated successfully"
}
```

**Validation:**
- The `name` field is required.
- The name cannot be empty.

### 3. Generate Password

**POST** `/password/`

Generates a password based on the requested length and character preferences.

**Request Body:**

```json
{
    "length": 16,
    "include_uppercase": true,
    "include_lowercase": true,
    "include_numbers": true,
    "include_symbols": true
}
```

**Example Response:**

```json
{
    "password": "CIpWOlk3/8[:'!Il",
    "length": 16,
    "message": "The password is generated"
}
```

**Validation:**
- Password length must be valid.
- At least one character category must be enabled.
- Character category options must be Boolean values (`true` or `false`).

## Testing the API

You can test the endpoints using:

- Django REST Framework's Browsable API.
- Postman.
- Thunder Client (VS Code extension).

For JSON requests, make sure to use:

```http
Content-Type: application/json
```

## Project Structure

```text
project/
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── generator/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

## Notes

- This project does not require a database for username or password generation.
- The Django development server is intended for local development and testing.
- Do not use the development server as a production deployment server.

## Author

Developed as a backend development challenge using Django and Django REST Framework.
