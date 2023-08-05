#!/bin/bash
set -e

#export PYTHONPATH=`dirname $0`
export PYTHONPATH=/vagrant/tests/integration/

echo "Starting celery workers..."
export CELERY_BROKER=redis://
#celery multi start 1 -A tasks -l info --pidfile=/var/run/%n.pid

echo "Starting flower..."
#python -m flower -A tasks &
#echo $1 > /var/run/flower.pid
sleep 3

echo "Calling tasks..."
for i in {1..10};
do
    celery -A tasks call tasks.add --args="[$i, $i]";
done
celery -A tasks call tasks.error --args="[\"My bad\"]"
celery -A tasks call tasks.sleep --args="[250]";
