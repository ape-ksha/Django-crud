FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /master
WORKDIR /master
COPY . /master/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD    python manage.py makemigrations && python manage.py migrate  && python manage.py runserver  0.0.0.0:8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_mongodb.app.wsgi"]