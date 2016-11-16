#!/bin/bash
KERAS_BACKEND=theano python epoch.py $1 
KERAS_BACKEND=theano python validcansurpassbaseline.py $1 $2
