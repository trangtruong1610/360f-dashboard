#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
source "$SH/.config.sh"

docker rm -f $CONTAINER_NAME || true  # remove container if exists

echo

docker run -d                  --name $CONTAINER_NAME   -p $PORT:5000    $IMAGE_TAG
#          run as background   container name           set api port     image to run

echo; sleep 1

docker logs $CONTAINER_NAME
