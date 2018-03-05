FROM python:3.6

WORKDIR /source

COPY requirements.txt ./

COPY gunicorn_config.py ./

RUN pip install -r requirements.txt

COPY source /app

EXPOSE 5100

CMD ["gunicorn", "--config", "./gunicorn_config.py", "app:app"]