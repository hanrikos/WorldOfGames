FROM python:3
RUN git clone https://github.com/ #TODO add repo
WORKDIR mygit # TODO add repo folder

CMD ["cat", "./Scores.txt"]
CMD [ "python3", "./MainScores.py" ]

