#!/bin/sh

compile() {
    PROGRAM=$1
    g++ -std=c++11 -O2 -Wall $PROGRAM.cpp -o $PROGRAM
}

compile $1
