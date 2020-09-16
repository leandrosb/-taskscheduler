FROM leandrosb/python:3.8-alpine

WORKDIR /app

ADD taskscheduler /app/taskscheduler
COPY requirements.txt /app
COPY wsgi.py /app


RUN pip install -r requirements.txt


ENV APP_ENV local

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]