FROM python:3.6

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--chdir", "source", "--config", "./gunicorn_config.py", "app:app"]
