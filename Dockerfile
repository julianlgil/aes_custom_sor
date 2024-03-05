FROM python:3.11-slim
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Instalar uvicorn
RUN pip install uvicorn
WORKDIR /app
