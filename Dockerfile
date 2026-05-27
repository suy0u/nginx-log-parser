FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["python", "parser.py", "--log", "nginx.log"]