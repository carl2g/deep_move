#!/bin/sh

volume_local="/tmp/deep_move"
volume_docker="/tmp/deep_move"

docker build -f Dockerfiles/Dockerfile-test -t deep_move_test .
docker run -t deep_move_test python -m unittest discover -s tests
