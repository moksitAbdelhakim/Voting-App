FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./templates /app/templates

EXPOSE 5000

CMD ["python", "vote.py"]
