FROM python:3.8-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8777

COPY . /app

ENTRYPOINT ["python"]

CMD ["./MainScores.py"]

