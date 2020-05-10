#!/usr/bin/env bash
cSH=`cd $(dirname $BASH_SOURCE) && pwd`
cAH=`cd $cSH/.. && pwd`

export      IMAGE_TAG=${IMAGE_TAG:-trang/aqa_api}
export CONTAINER_NAME=${CONTAINER_NAME:-trang_aqa_api}
export           PORT=20510
