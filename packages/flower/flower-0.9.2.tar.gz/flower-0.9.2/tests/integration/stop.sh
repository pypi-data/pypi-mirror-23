#!/bin/bash
set -e

echo "Stopping flower..."
echo kill -9 `cat /var/run/flower.pid`

echo "Stopping celery workers..."
celery multi stop 1 -A tasks -l info --pidfile=/var/run/celery%n.pid
