FROM python:3.6

WORKDIR /source

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY source /app

EXPOSE 8005
CMD [ "python", "app.py" ]