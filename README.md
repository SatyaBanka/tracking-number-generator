# Parcel Tracking Number Generator API
# 📦 Tracking Number Generator API

A scalable Django REST API that generates **unique tracking numbers** for parcels based on request metadata.  
It uses hash-based generation with constraints and is optimized for horizontal scaling.

---

## 🔧 Features

- Unique tracking number generation (Regex: `^[A-Z0-9]{1,16}$`)
- Hashing logic based on origin, destination, customer info, and timestamp
- High-performance and concurrent-safe
- Swagger/OpenAPI documentation available at `/docs/`

---

## 🚀 Tech Stack

- Python 3.11
- Django REST Framework
- Docker & Docker Compose
- Swagger for API documentation

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🛠️ Getting Started
---
### 1. Clone the repo

```bash
git clone https://github.com/your-username/tracking-number-generator.git
cd tracking-number-generator/parcel-tracking
---

### 2.Run the app locly with Docker
```bash
docker-compose up --build -d
---

### 3. Apply migrations and create superuser (optional)
In a new terminal:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
---
### 4. API Swagger/OpenAPI documentation

http://localhost:8000/docs/

![image](https://github.com/user-attachments/assets/1af403e3-122e-4511-a23b-28c4ad0e661b)

- Use API docs for testing API

