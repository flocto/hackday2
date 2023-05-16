FROM python:3.10-slim-buster

RUN mkdir /app
WORKDIR /app

COPY app.py /app
COPY feedback.html /app
COPY inspect.html /app

RUN pip install flask

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]