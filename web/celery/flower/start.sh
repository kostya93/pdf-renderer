#!/usr/bin/env bash

sleep 10
celery flower \
    --app=web \
    --broker="${REDIS_URL}" \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
