# Products Tracker

A full-stack CRUD application for managing products with search and sorting capabilities. Built with React, FastAPI, and PostgreSQL.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![React](https://img.shields.io/badge/React-18+-61dafb.svg)

---

## 🚀 Features

### Frontend (React)
- ✅ Create, read, update, and delete products
- 🔍 Search by ID, name, or description
- 🔄 Sort by ID, name, price, or quantity
- ⚡ Real-time success/error notifications
- 📱 Responsive design
- 🎨 Clean, intuitive UI

### Backend (FastAPI)
- 🔌 RESTful API with full CRUD operations
- 📊 SQLAlchemy ORM with PostgreSQL
- ✅ Input validation with Pydantic
- 🔒 CORS configuration for frontend
- 📝 Auto-generated API documentation (Swagger/OpenAPI)
- 🛡️ Proper error handling and HTTP status codes

### Database (PostgreSQL)
- 🗄️ Robust relational database
- 🔑 Auto-incrementing primary keys
- 📈 Scalable data persistence

---

## 📋 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React, Axios, CSS3 |
| **Backend** | FastAPI, SQLAlchemy, Pydantic |
| **Database** | PostgreSQL 14+ |
| **Dev Tools** | Uvicorn, npm, pgAdmin |

---

## 📁 Project Structure

```
products-tracker/
│
├── backend/
│   ├── main.py                 # FastAPI application & routes
│   ├── database.py             # Database connection & session
│   ├── database_models.py      # SQLAlchemy ORM models
│   ├── models.py               # Pydantic schemas
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js              # Main React component
│   │   ├── TaglineSection.js   # UI components
│   │   ├── App.css             # Styling
│   │   └── index.js
│   ├── package.json
│   └── .env.example
│
└── README.md
```

---

## 🛠️ Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.9+
- Node.js 16+ and npm
- PostgreSQL 14+
- pgAdmin (optional, for database management)

### 1️⃣ Database Setup

1. Start PostgreSQL service:
   ```bash
   # macOS (Homebrew)
   brew services start postgresql
   
   # Linux
   sudo systemctl start postgresql
   
   # Windows
   # Start from Services or pgAdmin
   ```

2. Create a database:
   ```bash
   psql -U postgres
   ```
   ```sql
   CREATE DATABASE products_db;
   \q
   ```

3. Update connection string in `backend/database.py` if needed:
   ```python
   DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/products_db"
   ```

### 2️⃣ Backend Setup (FastAPI)

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   # macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
   
   # Or use requirements.txt
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

5. Verify backend is running:
   - API: http://localhost:8000
   - Swagger Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### 3️⃣ Frontend Setup (React)

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm start
   ```

4. Access application:
   - Frontend: http://localhost:3000

---

## 🔌 API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `GET` | `/products` | Get all products | - |
| `GET` | `/products/{id}` | Get product by ID | - |
| `POST` | `/products` | Create new product | `ProductCreate` |
| `PUT` | `/products/{id}` | Update product | `ProductCreate` |
| `DELETE` | `/products/{id}` | Delete product | - |

### Example Request Bodies

**Create Product** (`POST /products`):
```json
{
  "name": "Monitor",
  "description": "24-inch LED display",
  "price": 199.99,
  "quantity": 15
}
```

**Update Product** (`PUT /products/{id}`):
```json
{
  "name": "Monitor",
  "description": "27-inch 4K display",
  "price": 349.99,
  "quantity": 10
}
```

### Response Format

**Success** (200/201):
```json
{
  "id": 1,
  "name": "Monitor",
  "description": "27-inch 4K display",
  "price": 349.99,
  "quantity": 10
}
```

**Error** (400/404/500):
```json
{
  "detail": "Product with ID 999 not found"
}
```

---

## 🐛 Common Issues & Solutions

### 1. CORS Errors
**Problem:** Browser blocks requests from React to FastAPI

**Solution:** Ensure CORS middleware is properly configured in `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 2. Database Connection Errors
**Problem:** `psycopg2.OperationalError: connection refused`

**Solution:**
- Verify PostgreSQL is running: `pg_isready`
- Check connection string in `database.py`
- Ensure database exists: `psql -l`

### 3. Port Already in Use
**Problem:** `Address already in use` error

**Solution:**
```bash
# Find and kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn main:app --reload --port 8001
```

### 4. Module Not Found Errors
**Problem:** Import errors in Python/Node

**Solution:**
```bash
# Backend
pip install -r requirements.txt

# Frontend
rm -rf node_modules package-lock.json
npm install
```

---

## 🚧 Known Limitations & Future Improvements

### Current Limitations
- ❌ No authentication/authorization
- ❌ No pagination for large datasets
- ❌ No file upload support (e.g., product images)
- ❌ No advanced filtering (price range, etc.)

### Planned Enhancements
- [ ] Add JWT authentication
- [ ] Implement pagination and filtering
- [ ] Add product image uploads
- [ ] Docker containerization
- [ ] Unit and integration tests
- [ ] CI/CD pipeline
- [ ] Rate limiting
- [ ] Caching layer (Redis)
- [ ] Advanced search with Elasticsearch

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

---

## 📦 Deployment

### Using Docker (Recommended)

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

### Manual Deployment

**Backend (Render/Railway/Heroku):**
- Set environment variables
- Use production WSGI server (Gunicorn)
- Configure DATABASE_URL

**Frontend (Vercel/Netlify):**
- Update API base URL to production backend
- Build production bundle: `npm run build`

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

## 👨‍💻 Author

**Divakar BV**

- GitHub: [@divakar-bv](https://github.com/divakar-bv)
- LinkedIn: [Divakar BV](https://linkedin.com/in/divakar-bv)

---

## 🙏 Acknowledgments

- FastAPI framework for excellent async support
- React team for the powerful UI library
- PostgreSQL community for the robust database
- All contributors and testers

---

## 📸 Screenshots

### Main Interface
*Add product listing with search and sort*

### Add/Edit Product
*Modal form for creating and updating products*

### Database View
*pgAdmin showing persisted data*

---

**⭐ If you find this project helpful, please give it a star!**
