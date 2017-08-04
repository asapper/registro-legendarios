#!/bin/bash

docker-compose up --build db &
docker-compose build web
docker-compose up web
