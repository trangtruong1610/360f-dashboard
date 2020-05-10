#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
source "$SH/.config.sh"

docker rm -f $CONTAINER_NAME || true  # remove container if exists

echo

docker run -d                  --name $CONTAINER_NAME   $IMAGE_TAG
#          run as background   container name           run this image

echo; sleep 1

docker logs $CONTAINER_NAME
