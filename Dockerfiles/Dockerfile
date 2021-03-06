FROM python:3.9-slim

COPY requirement.txt /requirement.txt
RUN pip install -r /requirement.txt

COPY deep_move /deep_move
COPY dataset /dataset
COPY examples /examples

WORKDIR /

CMD python /deep_move/train.py