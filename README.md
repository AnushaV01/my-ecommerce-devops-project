# 🐳 Dockerized Flask User Microservice

This branch contains the **Dockerized version** of the `user-service` microservice using a lightweight and secure Python base image.

> 🛠 Easily portable and production-ready Flask API, containerized for consistent deployment.

---

## 📌 Features

- Lightweight `python:3.11-slim` base image
- Isolated environment via Docker
- `.dockerignore` to reduce build context
- Health-checked Flask API on port 5050

---

## 🧱 Tech Stack

- Python 3.11
- Flask
- Docker
- `python-dotenv`

---

## 🐳 Docker Instructions

### 1. Build the Docker image

From inside the `user-service/` directory:

```bash
docker build -t user-service .

### 2. Run the container
```bash
docker run -d -p 5050:5050 --name user-service-container user-service

-d runs it in the background
-p 5050:5050 maps local port to container port
--name gives it a readable name

### 3. Test the API
add a user
```bash
curl -X POST http://localhost:5050/users \
-H "Content-Type: application/json" \
-d '{"name": "Jones", "email": "Jones@example.com"}'

get users list
```bash
curl http://localhost:5050/users


