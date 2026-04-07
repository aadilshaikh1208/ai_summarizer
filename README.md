# AI Text Summarizer with Asynchronous Processing

## 📌 Project Overview

This project is developed as part of the Software Engineer Intern practical assignment for RD Tech Innovation.

It is a web-based application that allows users to submit large text inputs and receive AI-generated summaries. The system processes tasks asynchronously using Celery and Redis, ensuring a non-blocking user experience.

---

## 🚀 Features

* Submit large text for summarization
* Background processing using Celery
* Task lifecycle tracking:

  * Pending
  * Processing
  * Completed
  * Failed
* View all submitted tasks
* Detailed task view with summary output
* REST API endpoints for task submission and status tracking

---

## 🧠 Tech Stack

* Backend: Django, Django REST Framework
* Asynchronous Processing: Celery
* Message Broker: Redis
* AI Model: Groq (LLaMA 3.1 via LangChain)
* Frontend: Django Templates (HTML, CSS)

---

## ⚙️ System Architecture

The application follows an asynchronous processing architecture:

User → Django Server → Redis Queue → Celery Worker → Database Update → UI/API Response

* Django handles incoming requests and stores tasks
* Redis acts as a message broker
* Celery processes long-running summarization tasks
* Task status is updated in the database and reflected in UI/API

---

## 🏗️ Project Structure

```
ai_summarizer/
│
├── manage.py
├── requirements.txt
├── .env
├── db.sqlite3
│
├── ai_summarizer/
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
└── summarizer/
    ├── models.py
    ├── views.py
    ├── tasks.py
    ├── urls.py
    └── templates/
        └── summarizer/
            └── index.html
```

---

## 🛠️ Setup Instructions (Local)

### 1. Clone Repository

```
git clone <your-repo-url>
cd ai_summarizer
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
SECRET_KEY=django-secret-key-here

```

---

### 5. Start Redis Server

Make sure Redis is running locally:

```
redis-server
```

---

### 6. Apply Migrations

```
python manage.py migrate
```

---

### 7. Run Django Server

```
python manage.py runserver
```

---

### 8. Start Celery Worker (IMPORTANT)

```
celery -A ai_summarizer worker --pool=solo --loglevel=info
```

(Note: `--pool=solo` is required for Windows systems)

---

## 🌐 API Endpoints

### Submit Task

POST `/api/submit/`

### Get Task Status

GET `/api/status/<task_id>/`

### Get All Tasks

GET `/api/tasks/`

### Get Task Details

GET `task/<str:task_id>/`

---

## 📊 Task Lifecycle

Each task follows this lifecycle:

1. Pending → Task created
2. Processing → Celery worker is executing
3. Completed → Summary generated successfully
4. Failed → Error occurred during processing

---

## ⚠️ Assumptions

* Redis is installed and running locally
* GROQ API key is valid
* SQLite is used for simplicity
* Celery worker runs separately from Django server

---

## 🚧 Limitations

* No authentication system
* No rate limiting
* SQLite is not production-grade
* No deployment configured (demonstrated locally), because there is no way to deploy redis worker other than aws or any other cloud platform (which is paid). 

---

## 🎥 Demo

A screen recording is included demonstrating:

* Submitting text for summarization
* Background processing via Celery
* Task status updates
* Final summary output

---

## ✅ Conclusion

This project demonstrates:

* Asynchronous task execution using Celery and Redis
* Non-blocking backend design
* Integration of AI-based summarization
* Clean and modular Django architecture

---
