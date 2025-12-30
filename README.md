# Inventory Tracker – FastAPI + React + PostgreSQL

A full-stack **Inventory Management CRUD application** built using **FastAPI**, **React**, and **PostgreSQL**.  
The application allows users to **add, view, update, search, and delete products** through a RESTful API and a responsive frontend UI.

---

## 🚀 Tech Stack

### Backend
- **FastAPI**
- **Python**
- **SQLAlchemy (ORM)**
- **PostgreSQL**
- **Pydantic**
- **Uvicorn**

### Frontend
- **React**
- **JavaScript**
- **HTML / CSS**
- **Fetch API**

### Tools
- Git & GitHub  
- VS Code  
- pgAdmin  

---

## ✨ Features

- Create new products
- View all products
- Search products by name
- Update product details
- Delete products
- RESTful API design
- PostgreSQL database integration
- Interactive API docs (Swagger UI)

---

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| GET    | `/`              | Health check     |
| GET    | `/products`      | Get all products |
| POST   | `/products`      | Create product   |
| PUT    | `/products/{id}` | Update product   |
| DELETE | `/products/{id}` | Delete product   |


📌 Future Improvements

1.Authentication & authorization
2.Pagination
3.Dockerization
4.Deployment (Render / Railway / Vercel)
5.Unit & integration tests
