# Secure Flask User Microservice – DevSecOps Edition

This is the enhanced version of the `user-service` microservice, built with security and clean architecture in mind.

> 🔒 Implements basic DevSecOps best practices like input validation, `.env` usage, and production-safe configuration.

---

## 📌 Features

- REST API with Flask
- Routes:
  - `GET /users` – List all users
  - `POST /users` – Add a new user
- Input validation for required fields (`name`, `email`)
- Removes leading/trailing whitespace using `.strip()`
- Uses UUIDv4 for unique user IDs
- `.env` file support (for port configuration)
- Debug mode disabled (`debug=False`)
- Clean project structure and readable code

---

## 🧱 Tech Stack

- Python 3.11
- Flask
- `python-dotenv`

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/anushavendra/my-ecommerce-devops-project.git
cd my-ecommerce-devops-project/user-service

