FROM python:3.7

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

WORKDIR /hk-fastapi-monitoring

COPY . /hk-fastapi-monitoring

EXPOSE 80

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]