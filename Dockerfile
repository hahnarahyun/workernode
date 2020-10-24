FROM python:3.4

ADD . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt

CMD ["echo", "hello"]