




FROM python:3

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:5001"]

##
