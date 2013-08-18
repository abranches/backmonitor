#!/bin/bash
DIR="../proto_classes"
if [ ! -x $DIR ]; then
    mkdir $DIR
    touch $DIR
fi

protoc --python_out=$DIR *.proto
