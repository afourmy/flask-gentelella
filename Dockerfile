FROM python:3.6

ENV FLASK_APP gentelella.py

RUN adduser -D gentelella

USER gentelella

WORKDIR /home/gentelella

COPY requirements.txt ./

COPY gunicorn_config.py ./

COPY app app

COPY migrations migrations

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--chdir", "app", "--config", "./gunicorn_config.py", "app:app"]
