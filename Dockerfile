FROM python:3

RUN pip install requirements.txt

COPY . .

# RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:5001"]