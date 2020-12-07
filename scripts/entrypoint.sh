#!/bin/bash
gunicorn tjet.wsgi:application --bind "0.0.0.0:$PORT" --env DJANGO_SETTINGS_MODULE=tjet.settings.production
