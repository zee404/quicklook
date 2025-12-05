FROM python:3.11-slim

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY . .

CMD ["fastapi", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
