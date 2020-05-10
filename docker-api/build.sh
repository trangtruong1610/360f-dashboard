#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
AH=`cd $SH/.. && pwd`

source "$SH/.config.sh"

docker build   --file "$SH/Dockerfile"      -t $IMAGE_TAG   $AH
#              build from this Dockerfile   image tag       set :pwd for Dockerfile
