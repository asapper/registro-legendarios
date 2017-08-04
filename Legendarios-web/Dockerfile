FROM python:2.7
ENV PYTHONUNBUFFERED 1
# directory to store code
RUN mkdir /code

WORKDIR /code
# install packages
ADD requirements.txt /code/
RUN pip install -r requirements.txt
# copy over code
COPY . /code/
