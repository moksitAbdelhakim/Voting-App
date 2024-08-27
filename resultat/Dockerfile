FROM python:3.8 

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN ["pip", "install", "-r", "requirements.txt"]

COPY ./templates /app/templates

EXPOSE 5001

CMD ["python", "resultat.py"]

