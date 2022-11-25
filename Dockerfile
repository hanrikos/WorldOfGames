FROM python:3.8-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5012

COPY . /app

RUN ["pwd"]
RUN ["ls" ,"-la"]

CMD ["python", "MainGame.py"]


