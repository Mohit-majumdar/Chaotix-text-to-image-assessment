# Chaotix-text-to-image-assessment
this repo in for assessment of chaotix.ai

---

# Django Image Generation Project

## Overview
This project demonstrates the use of Django, Celery, and Redis to generate images using the Stability AI API. It involves setting up a Django application, integrating Celery for asynchronous task management, and saving the generated images in the local filesystem.

## Features
- Handling mutliple requests parallel execution
- Asynchronous image generation using Celery and Redis
- Integration with Stability AI's Text-to-Image API
- Image storage using Django's media handling
 

## Requirements
- Python 3.x
- Django
- Redis
- Celery
- Stability AI API Key

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Mohit-majumdar/Chaotix-text-to-image-assessment/.git
cd Chaotix-text-to-image-assessment/
```

### 2. Install Dependencies
Create a virtual environment and install the required Python packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Redis Installation
Ensure that Redis is installed and running on your machine. 

**On Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install redis-server
sudo systemctl start redis-server
```

**On macOS with Homebrew:**
```bash
brew install redis
brew services start redis
```

### 4. Project Configuration
Copy the sample environment file and update the necessary environment variables:
```bash
cp .env.sample .env
```

Edit `.env` to include your Stability AI API Key and other configuration settings:
```env
STABILITY_API_KEY=your_stability_ai_api_key
```

### 5. Django Setup
Migrate the database and collect static files:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

### 6. Running the Application

#### Start the Django Development Server
```bash
python manage.py runserver
```

#### Start Celery Worker
```bash
celery -A chaotix_text_to_image worker -l info
```
#### Send Post request 
- open browser and go to http://127.0.0.1:8000/api/generate-images/
- send a post request body schema: {"Prompt":[ array of prompts  ]}

### 7. Usage
You can trigger the image generation by accessing the appropriate Django view or API endpoint. The images will be processed asynchronously by Celery and stored locally in the `media/` directory.

## Notes
- Ensure that Redis is running before starting the Celery worker.
- For production deployment, consider setting up a more robust solution for media storage, such as using a cloud storage service.
- Configure proper security measures, including secure storage of the API key and setting up HTTPS for secure communication.
