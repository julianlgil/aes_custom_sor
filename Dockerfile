FROM python:3.11

# Instalar uvicorn
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl -f http://localhost:$APP_PORT/health || exit 1

EXPOSE $APP_PORT
CMD uvicorn main:app --host 0.0.0.0 --port "${APP_PORT}" --reload