FROM python:3.6

ENV FLASK_APP gentelella.py

COPY gentelella.py gunicorn.py requirements.txt ./
COPY app app
COPY migrations migrations

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "--config", "gunicorn.py", "gentelella:app"]