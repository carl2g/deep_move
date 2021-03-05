#!/bin/sh

if [ ! -z $1 ]
then
	volume_local="/tmp/deep_move"
	volume_docker="/tmp/deep_move"
	docker build -f Dockerfiles/Dockerfile -t deep_move . && \
	docker run --volume $volume_local:$volume_docker deep_move python ./predict.py $1 && \
	cp $volume_local/prediction.json .
else
	echo "Missing argument:"
	echo "\tPlease give the absolute path of the image to classify"
fi