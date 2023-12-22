FROM python:3.11.5

WORKDIR /Oficina

COPY . .

RUN pip install django
RUN pip install mysqlclient
RUN pip install fpdf
RUN pip install dj_database_url
RUN pip install psycopg2

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]