# ---- Build Stage ----
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---- Runtime Stage ----
FROM python:3.11-slim

# Create a non-root user
RUN groupadd -r botuser && useradd -r -g botuser botuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /home/botuser/.local

# Ensure local binaries are on PATH
ENV PATH=/home/botuser/.local/bin:$PATH

# Copy application code
COPY --chown=botuser:botuser . .

# Switch to non-root user
USER botuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD pgrep -f "python main.py" || exit 1

CMD ["python", "main.py"]
