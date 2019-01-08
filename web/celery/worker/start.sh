#!/usr/bin/env bash

sleep 10
celery -A web worker -l INFO
