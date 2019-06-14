#!/bin/bash

function create() {
    cd /home/ravi/Documents
    python create.py $1
    cd /home/ravi/Documents/$1
    code .
    cd
}

function delete () {
    cd /home/ravi/Documents
    python delete.py $1
    cd
}