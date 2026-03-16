# 🎬 CSCE 548 — Movie Watchlist Application

A full-stack, 4-tier movie watchlist application built for CSCE 548 at the University of South Carolina. Built with AI assistance (Claude by Anthropic) as part of an exercise in AI-assisted software development.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  Client Layer       HTML + JavaScript (port 5500)   │
├─────────────────────────────────────────────────────┤
│  Service Layer      FastAPI + Uvicorn (port 8000)   │
├─────────────────────────────────────────────────────┤
│  Business Layer     Python — validation rules       │
├─────────────────────────────────────────────────────┤
│  Data Layer (DAL)   Python — mysql-connector        │
├─────────────────────────────────────────────────────┤
│  Database           MySQL 8 — csce548_watchlist     │
└─────────────────────────────────────────────────────┘
```

---

## Repository Structure

```
CSCE548/
├── project2/src/          # Backend (FastAPI service)
│   ├── service.py         # REST API endpoints
│   ├── business.py        # Business rules & validation
│   ├── db.py              # MySQL connection
│   ├── requirements.txt
│   └── dal/
│       ├── movies_dao.py  # Movies CRUD
│       └── lists_dao.py   # Watchlists CRUD
├── project3/frontend/     # Frontend
│   ├── index.html         # Single-page app UI
│   └── app.js             # API calls (legacy)
├── sql/
│   ├── 01_schema.sql      # Database schema
│   └── 02_seed.sql        # Sample data (50+ rows)
└── README.md
```

---

## Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.9+ |
| MySQL Community Server | 8.0+ |
| pip | bundled with Python |
| Git | any recent version |
| Web browser | Chrome, Firefox, or Safari |

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/2teaS/CSCE548.git
cd CSCE548
```

### 2. Start MySQL
```bash
# macOS (Homebrew)
brew services start mysql

# macOS (official installer)
sudo /usr/local/mysql/support-files/mysql.server start

# Linux
sudo systemctl start mysql
```

### 3. Set up the database
```bash
mysql -u root -p
```
Inside MySQL:
```sql
SOURCE /full/path/to/CSCE548/sql/01_schema.sql;
SOURCE /full/path/to/CSCE548/sql/02_seed.sql;
EXIT;
```

### 4. Configure the database connection
Edit `project2/src/db.py` and update:
```python
password = "YourMySQLPasswordHere"
```

### 5. Install Python dependencies
```bash
cd project2/src
pip install -r requirements.txt
```

### 6. Start the backend
```bash
uvicorn service:app --reload --port 8000
```
✅ You should see: `Uvicorn running on http://127.0.0.1:8000`

Interactive API docs available at: `http://127.0.0.1:8000/docs`

### 7. Serve the frontend
Open a second terminal:
```bash
cd project3/frontend
python -m http.server 5500
```
Then open your browser to: **http://127.0.0.1:5500/index.html**

Click **Ping** — the status indicator should turn green ✅

---

## Features

- **Movies** — Create, read, update, and delete movie records
- **Watchlists** — Create and manage user watchlists
- **Filter** — Filter movies by genre
- **Quick actions** — Edit and Delete buttons directly in the movie table
- **Validation** — Business rules enforced (year range, required fields, etc.)
- **User-friendly UI** — Clean response cards instead of raw JSON

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/movies` | List all movies |
| GET | `/movies/{id}` | Get a single movie |
| POST | `/movies` | Create a movie |
| PUT | `/movies/{id}` | Update a movie |
| DELETE | `/movies/{id}` | Delete a movie |
| GET | `/users/{user_id}/lists` | Get a user's watchlists |
| POST | `/users/{user_id}/lists` | Create a watchlist |
| PUT | `/lists/{list_id}` | Rename a watchlist |
| DELETE | `/lists/{list_id}` | Delete a watchlist |
| GET | `/lists/{list_id}/items` | Get movies in a list |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Frontend shows "Server unreachable" | Make sure uvicorn is running on port 8000 |
| MySQL connection error | Check credentials in `db.py`; try removing the `unix_socket` line on macOS |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` from `project2/src/` |
| CORS error in browser | Serve the frontend via `http://` (not `file://`) using `python -m http.server 5500` |
| Port 8000 already in use | Run `lsof -ti:8000 \| xargs kill -9` then restart uvicorn |

---

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) — Python REST framework
- [Uvicorn](https://www.uvicorn.org/) — ASGI server
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/) — MySQL driver
- [Pydantic](https://docs.pydantic.dev/) — Data validation
- AI assistance by [Claude](https://claude.ai) (Anthropic)

---

*CSCE 548 — Database Systems | University of South Carolina | Spring 2026*
