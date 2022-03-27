FROM python:3.8.10-alpine
WORKDIR /usr/src/app
COPY . .
ENTRYPOINT [ "python", "./main.py" ]