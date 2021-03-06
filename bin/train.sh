#!/bin/sh

volume_local="/tmp/deep_move"
volume_docker="/tmp/deep_move"

docker build -f Dockerfiles/Dockerfile -t deep_move .
docker run --volume $volume_local:$volume_docker -t deep_move python -m deep_move.train
