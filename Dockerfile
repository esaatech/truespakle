FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

WORKDIR /app

# Install poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install production dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy application code
COPY . .

# Expose the port
EXPOSE ${PORT}

# Run the application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 wsgi:app 