FROM python:3.11-slim

ARG BUILD_ENV=production
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    BUILD_ENV=${BUILD_ENV} \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash app

COPY requirements.txt .

RUN pip install --prefix=/local -r requirements.txt \
    && find /local -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true \
    && find /local -type f -name "*.pyc" -delete

COPY --chown=app:app . .

RUN if [ "$BUILD_ENV" = "production" ]; then \
        pip install --prefix=/local --no-deps -r requirements.txt 2>/dev/null || true; \
    fi

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
