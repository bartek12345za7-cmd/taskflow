# TaskFlow API

![Status](https://img.shields.io/badge/status-production--ready-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)

Production-ready Task Management REST API built with FastAPI, PostgreSQL, and Docker. Designed as a portfolio project demonstrating professional DevOps practices, clean architecture, and production security standards.

## 🎯 Purpose

This project serves as a **portfolio demonstration** of:
- Multi-container Docker orchestration
- RESTful API design with FastAPI
- JWT authentication & security best practices
- Database connection pooling & optimization
- Infrastructure-as-Code with Docker Compose
- Production-grade configuration management

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Load Balancer                          │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Nginx     │         │   Nginx     │         │   Nginx     │
│  (Frontend) │         │  (Frontend) │         │  (Frontend) │
└─────────────┘         └─────────────┘         └─────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                    ┌───────┴───────┐
                    ▼               ▼
            ┌─────────────┐   ┌─────────────┐
            │   FastAPI   │   │   FastAPI   │
            │  (Backend)  │   │  (Backend)  │
            └─────────────┘   └─────────────┘
                    │               │
                    └───────┬───────┘
                            ▼
                    ┌─────────────┐
                    │ PostgreSQL  │
                    │  (Database) │
                    └─────────────┘
```

## Tech Stack

| Component | Technology | Version |
|-----------|------------|---------|
| Backend | FastAPI | 0.109.0 |
| Database | PostgreSQL | 15 |
| Frontend | Nginx | Alpine |
| Container | Docker | Compose v3.8 |
| Auth | JWT (python-jose) | 3.3.0 |
| ORM | SQLAlchemy | 2.0.25 |

## Features

### Security
- [x] JWT authentication with bcrypt password hashing
- [x] Rate limiting (60 requests/minute per IP)
- [x] CORS whitelist configuration
- [x] Security headers (CSP, X-Frame-Options, X-Content-Type-Options)
- [x] Non-root Docker containers
- [x] SSL/TLS support for database connections

### Performance
- [x] Database connection pooling (QueuePool)
- [x] Connection pre-ping and recycle
- [x] Database indexes on frequently queried columns
- [x] Pagination support for list endpoints
- [x] Resource limits in Docker Compose

### DevOps
- [x] Multi-stage Docker builds
- [x] Health checks for all services
- [x] Environment-based configuration
- [x] Development and Production compose files

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)

### Development

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/taskflow.git
cd taskflow

# Setup environment
cp backend/.env.example backend/.env
# Edit .env with your values

# Start all services
docker compose up --build

# API available at http://localhost:8000
# Swagger docs at http://localhost:8000/docs
# Frontend at http://localhost
```

### Production

```bash
# Use production compose file
docker compose -f docker-compose.prod.yml up --build

# Or with specific env file
POSTGRES_PASSWORD=your_secure_password \
SECRET_KEY=$(openssl rand -hex 32) \
docker compose -f docker-compose.prod.yml up --build
```

## API Reference

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login, returns JWT token |

### Tasks (requires authentication)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List user's tasks (paginated) |
| POST | `/tasks` | Create new task |
| DELETE | `/tasks/{id}` | Delete task |

### Health

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Service health check |

### Example Usage

```bash
# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","email":"demo@example.com","password":"SecurePass123!"}'

# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","password":"SecurePass123!"}'

# Create Task (with token)
curl -X POST http://localhost:8000/tasks \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Complete portfolio project"}'

# List Tasks
curl http://localhost:8000/tasks \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SECRET_KEY` | Yes | - | JWT signing key (min 32 characters) |
| `DATABASE_URL` | No | auto | PostgreSQL connection string |
| `POSTGRES_PASSWORD` | Yes | - | Database password |
| `CORS_ORIGINS` | No | `[]` | Allowed CORS origins array |
| `LOG_LEVEL` | No | `INFO` | Logging level |
| `RATE_LIMIT_PER_MINUTE` | No | `60` | Rate limit threshold |

## Project Structure

```
taskflow/
├── backend/
│   ├── main.py          # FastAPI application & routes
│   ├── auth.py          # JWT authentication & password hashing
│   ├── config.py        # Pydantic settings management
│   ├── database.py      # SQLAlchemy engine & session
│   ├── models.py        # SQLAlchemy ORM models
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html       # Single-page frontend
│   ├── nginx.conf       # Nginx configuration
│   └── Dockerfile
├── docker-compose.yml           # Development environment
├── docker-compose.prod.yml      # Production environment
├── .env.example
├── README.md
└── LICENSE
```

## Key Design Decisions

### Why FastAPI?
- Async support for high concurrency
- Automatic OpenAPI documentation
- Type safety with Pydantic validation
- Built-in dependency injection

### Why PostgreSQL?
- ACID compliance for data integrity
- JSON support for flexible data
- Excellent performance with proper indexing
- Industry standard for production APIs

### Why Docker Compose v3.8?
- Native support for resource limits
- Build secrets management
- Horizontal scaling with replicas
- Health checks integration

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Built as a portfolio project to demonstrate production-grade DevOps practices.*
