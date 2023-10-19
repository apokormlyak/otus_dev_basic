#docker build . -t app
#docker run  -p 8000:8000 app
FROM python:3.11.6-bookworm

WORKDIR /app

COPY . .

RUN pip install --upgrade pip "poetry==1.6.1"
RUN poetry config virtualenvs.create false


RUN poetry install

EXPOSE 8000

CMD ["uvicorn", "view.ping_ping:app", "--host", "0.0.0.0", "--port", "8000"]