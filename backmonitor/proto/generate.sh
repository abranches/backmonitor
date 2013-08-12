#!/bin/bash
if [ ! -x "../network_messages" ]; then
    mkdir ../network_messages
    touch ../network_messages/__init__.py
fi

protoc --python_out=../network_messages *.proto
