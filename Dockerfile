FROM python:3-alpine

ENV PORT=8000
EXPOSE $PORT

WORKDIR /app
COPY . /app
RUN pip install pipenv && pipenv install --system

CMD ["python3", "app.py"]
