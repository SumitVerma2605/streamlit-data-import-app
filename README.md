# 🐳 Dockerized Data Flow IDE

Professional data pipeline IDE with microservices architecture, containerized with Docker Compose.

## 🏗️ Architecture

```
┌─────────────┐     ┌──────────────┐     ┌────────────���─┐
│  Streamlit  │     │  FastAPI     │     │   Celery     │
│  Frontend   │────▶│  Backend     │────▶│  Processor   │
└─────────────┘     └──────────────┘     └──────────────┘
       │                   │                     │
       └───────────────────┴─────────────────────┘
                     │
          ┌──────────┴──────────┐
          │                     │
       ┌──────┐            ┌─────────┐
       │ PG   │            │ Redis   │
       └──────┘            └─────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- 4GB RAM minimum
- 2GB disk space

### Installation

```bash
# Clone repository
git clone <repo-url>
cd dockerized-ide

# Copy environment file
cp .env.example .env

# Start services
bash scripts/startup.sh
```

### Access Services

- **Frontend**: http://localhost
- **API Docs**: http://localhost/api/docs
- **Streamlit**: http://localhost:8501

## 📋 Services

### 1. **Nginx** (Port 80)
- Reverse proxy
- Load balancer
- Rate limiting

### 2. **FastAPI Backend** (Port 8000)
- RESTful API
- File upload handling
- Data transformation
- Export functionality

### 3. **Streamlit Frontend** (Port 8501)
- Interactive UI
- Real-time data preview
- Column operations

### 4. **Celery Processor**
- Async task queue
- Background processing
- Long-running operations

### 5. **PostgreSQL** (Port 5432)
- Metadata storage
- User data
- Transformation history

### 6. **Redis** (Port 6379)
- Caching
- Message broker
- Session storage

## 📖 API Documentation

### Upload Endpoint

```bash
curl -X POST http://localhost/api/upload/file \
  -F "file=@data.csv"
```

Response:
```json
{
  "file_id": "uuid",
  "rows": 1000,
  "columns": 15,
  "status": "success"
}
```

### Transform Endpoint

```bash
curl -X POST http://localhost/api/transform/column \
  -H "Content-Type: application/json" \
  -d '{
    "column_name": "age",
    "operation": "convert_type",
    "parameters": {"type": "numeric"}
  }'
```

## 🔧 Configuration

Edit `.env` file to customize:

```env
# Database
DB_USER=datauser
DB_PASSWORD=secure_password_123

# Redis
REDIS_PASSWORD=redis_secure_pass

# Upload
MAX_UPLOAD_SIZE_MB=500

# Environment
ENVIRONMENT=development
LOG_LEVEL=INFO
```

## 📦 Docker Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f backend

# Rebuild images
docker-compose build --no-cache

# Scale services
docker-compose up -d --scale processor=3

# Health check
docker-compose ps
```

## 🧪 Testing

```bash
# Run backend tests
docker-compose exec backend pytest

# Check API health
curl http://localhost/api/health

# Database connection
docker-compose exec postgres psql -U datauser -d dataflow -c "\dt"
```

## 📊 Monitoring

Access Prometheus metrics at port 9090 (if enabled)

```bash
# Check container resource usage
docker stats
```

## 🔐 Security

- Change default passwords in `.env`
- Enable SSL/TLS in production
- Use secrets management
- Rate limiting enabled
- CORS configured
- JWT authentication ready

## 🐛 Troubleshooting

### Services won't start
```bash
# Check Docker logs
docker-compose logs

# Rebuild everything
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Database connection error
```bash
# Reset database
docker-compose exec postgres psql -U datauser -d dataflow -f /migrations/reset.sql
```

### Port already in use
```bash
# Change ports in docker-compose.yml
# Or stop conflicting services
lsof -i :8000  # Find process using port
```

## 📝 License

MIT License

## 🤝 Contributing

1. Create feature branch
2. Commit changes
3. Push to branch
4. Create Pull Request

---

**Made with ❤️ for data professionals**