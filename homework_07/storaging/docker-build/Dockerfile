FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip

COPY ./storaging/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./storaging/docker-build/entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY . .

