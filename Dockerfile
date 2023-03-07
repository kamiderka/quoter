FROM python:3.7-slim
WORKDIR /src

COPY ../requirements.txt .

RUN pip install -r requirements.txt

RUN python manage.py migrate --run-syncdb

COPY . .

EXPOSE 8000

CMD ["gunicorn", "quoter.wsgi:application"]