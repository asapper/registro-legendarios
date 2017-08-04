#!/bin/bash

psql -U postgres -d postgres < docker-entrypoint-initdb.d/init.sql 
