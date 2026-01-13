# FastAPI + PostgreSQL — Backend Template

A **professional,backend boilerplate** built with **FastAPI** and **PostgreSQL**, designed for scalable, secure, and maintainable API development. This setup follows real‑world engineering practices including modular architecture, async DB access, migrations, environment‑based configuration, and container‑ready deployment.

<img width="1144" height="644" alt="Image" src="https://github.com/user-attachments/assets/bce26058-ee0b-40d0-aef9-926cba1920c5" />

---

## Key Features

* **FastAPI** for high‑performance async APIs
* **PostgreSQL** as a robust relational database
* **SQLAlchemy 2.0 (Async ORM)**
* **Alembic** for database migrations
* **Environment‑based configuration** using `.env`
* **Pydantic v2** schemas for validation & serialization
* **Clean, modular architecture** (router / service / db / models)
* Ready for **testing, Docker, and CI/CD**

---

## ⚙️ Tech Stack

| Layer         | Technology         |
| ------------- | ------------------ |
| API Framework | FastAPI            |
| Database      | PostgreSQL         |
| ORM           | SQLAlchemy (Async) |
| Migrations    | Alembic            |
| Validation    | Pydantic v2        |
| Server        | Uvicorn            |

---

## 🔧 Environment Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/fastapi_db
APP_NAME=FastAPI PostgreSQL Backend
DEBUG=True
```

---

## Database Setup

### Create Database

```sql
CREATE DATABASE fastapi_db;
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
alembic upgrade head
```

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Interactive docs:

* Swagger UI → `/docs`
* ReDoc → `/redoc`

---

## 📈 Scalability Notes

* Supports async concurrency
* Easy horizontal scaling behind a load balancer
* Clean separation of concerns
* Migration‑safe schema evolution

---

## 📄 License

MIT License — Free to use in personal and commercial projects.

---

## 👨‍💻 Author

**Md. Hasan Imon**
AI / ML Engineer

📧 [emon.mlengineer@gmail.com](mailto:emon.mlengineer@gmail.com)

🔗 [https://github.com/Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)

---