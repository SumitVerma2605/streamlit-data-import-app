#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║         🚀 Data Flow IDE - Dockerized Environment         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed${NC}"
    exit 1
fi

# Check Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose is not installed${NC}"
    exit 1
fi

echo -e "${YELLOW}📦 Building images...${NC}"
docker-compose build --no-cache

echo -e "${YELLOW}🚀 Starting services...${NC}"
docker-compose up -d

echo -e "${YELLOW}⏳ Waiting for services to be healthy...${NC}"
sleep 10

# Check health
echo -e "${YELLOW}🔍 Checking service health...${NC}"

services=("postgres" "redis" "backend" "frontend" "nginx")
for service in "${services[@]}"; do
    if docker-compose ps $service | grep -q "healthy\|running"; then
        echo -e "${GREEN}✅ $service is running${NC}"
    else
        echo -e "${RED}❌ $service is not healthy${NC}"
    fi
done

echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║              🎉 Services Started Successfully              ║"
echo "╠════════════════════════════════════════════════════════════╣"
echo "║  Frontend    → http://localhost                           ║"
echo "║  Backend API → http://localhost/api/docs                 ║"
echo "║  Streamlit   → http://localhost:8501                     ║"
echo "║  Postgres    → localhost:5432                            ║"
echo "║  Redis       → localhost:6379                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Show logs
echo -e "${YELLOW}📋 Showing logs... (Press Ctrl+C to exit)${NC}"
docker-compose logs -f