#!/bin/bash

echo $HOME
echo -n "Enter file name or pytest to run all: "
read var

python -m $var
exit_code=$?
if [[ $exit_code = 0 ]]; then
    echo "success"
    git add .
    git commit -m "shell scripting"
    git push
else
    echo "failure: $exit_code"
fi