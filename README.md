# AI Text Summarizer with Asynchronous Processing

## 📌 Project Overview
This project is developed as part of the Software Engineer Intern practical assignment for RD Tech Innovation.

It is a web-based application that allows users to submit large text inputs and receive AI-generated summaries. The system processes tasks asynchronously using Celery and Redis, ensuring a non-blocking user experience.

---

## 🚀 Features

- Submit large text for summarization
- Background processing using Celery
- Task lifecycle tracking:
  - Pending
  - Processing
  - Completed
  - Failed
- View all submitted tasks
- Detailed task view with summary output
- REST API endpoints for task submission and status tracking

---

## 🧠 Tech Stack

- Backend: Django, Django REST Framework
- Asynchronous Processing: Celery
- Message Broker: Redis
- AI Model: Groq (LLaMA 3.1 via LangChain)
- Frontend: Django Templates (HTML, CSS)

---

## ⚙️ System Architecture

The system follows an asynchronous task processing architecture:

User Request → Django Server → Redis Queue → Celery Worker → Database Update → Response

- Django handles user requests and API endpoints
- Redis acts as a message broker
- Celery processes long-running tasks in the background
- Task status is stored and updated in the database

Celery is integrated directly within the Django project, which is a standard approach for handling background jobs :contentReference[oaicite:0]{index=0}.

---

## 🏗️ Project Structure




# AI Text Summarizer with Asynchronous Processing

## 📌 Project Overview
This project is developed as part of the Software Engineer Intern practical assignment for RD Tech Innovation.

It is a web-based application that allows users to submit large text inputs and receive AI-generated summaries. The system processes tasks asynchronously using Celery and Redis, ensuring a non-blocking user experience.

---

## 🚀 Features

- Submit large text for summarization
- Background processing using Celery
- Task lifecycle tracking:
  - Pending
  - Processing
  - Completed
  - Failed
- View all submitted tasks
- Detailed task view with summary output
- REST API endpoints for task submission and status tracking

---

## 🧠 Tech Stack

- Backend: Django, Django REST Framework
- Asynchronous Processing: Celery
- Message Broker: Redis
- AI Model: Groq (LLaMA 3.1 via LangChain)
- Frontend: Django Templates (HTML, CSS)

---

## ⚙️ System Architecture

The system follows an asynchronous task processing architecture:

User Request → Django Server → Redis Queue → Celery Worker → Database Update → Response

- Django handles user requests and API endpoints
- Redis acts as a message broker
- Celery processes long-running tasks in the background
- Task status is stored and updated in the database

Celery is integrated directly within the Django project, which is a standard approach for handling background jobs :contentReference[oaicite:0]{index=0}.

---

## 🏗️ Project Structure



This follows a standard Django + Celery structure where tasks are defined inside the app and executed by workers :contentReference[oaicite:1]{index=1}.

---

## 🛠️ Setup Instructions (Local)

### 1. Clone Repository

git clone <your-repo-url>
cd ai_summarizer


---

### 2. Create Virtual Environment

python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows


---

### 3. Install Dependencies

pip install -r requirements.txt


---

### 4. Setup Environment Variables

Create a `.env` file:

SECRET_KEY=your-secret-key
DEBUG=True
GROQ_API_KEY=your-api-key
REDIS_URL=redis://localhost:6379/0


---

### 5. Run Redis Server
Make sure Redis is running locally


---

### 6. Run Migrations

python manage.py migrate

---

### 7. Start Django Server

python manage.py runserver

---

### 8. Start Celery Worker

celery -A ai_summarizer worker --pool=solo --loglevel=info


(Note: `--pool=solo` is required for Windows systems)

---

## 🌐 API Endpoints

### Submit Task

POST /api/submit/


### Get Task Status

GET /api/status/<task_id>/


### Get All Tasks

GET /api/tasks/


---

## 📊 Task Lifecycle

Each task goes through the following states:

1. Pending → Task created
2. Processing → Celery worker executing
3. Completed → Summary generated
4. Failed → Error occurred

---

## ⚠️ Assumptions

- Redis is available locally or via cloud service
- GROQ API key is valid and active
- SQLite is used for simplicity (not production-grade)
- Celery worker runs separately from Django server

---

## 🚧 Limitations

- No authentication system
- No rate limiting for API calls
- SQLite used instead of PostgreSQL
- Deployment of Celery workers may require paid services

---

## 🌍 Deployment Notes

Due to limitations of free-tier platforms, the application is best demonstrated locally with:
- Django running as web server
- Celery worker running separately
- Redis acting as message broker

The system can be deployed using services like Render with separate services for:
- Web server
- Celery worker
- Redis instance

---

## 🎥 Demo

A video demonstration is included showing:
- Task submission
- Background processing
- Status updates
- Final summary output

---

## ✅ Conclusion

This project demonstrates:
- Asynchronous task handling using Celery
- Non-blocking backend architecture
- Integration of AI services into web applications
- Clean and modular Django design

---