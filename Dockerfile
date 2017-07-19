FROM python:3
ENV PYTHONUNBUFFERED 1
# directory to store code
RUN mkdir /code
RUN mkdir /docker-entrypoint-initdb.d/
# copy init sql script
ADD init.sql /docker-entrypoint-initdb.d/

WORKDIR /code
# install packages
ADD requirements.txt /code/
RUN pip install -r requirements.txt
# copy over code
COPY . /code/
# migrate db
RUN python manage.py migrate
# init Groups and Permissions
RUN python manage.py shell < init-script.py
