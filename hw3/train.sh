#!/bin/bash
python epoch.py $1 
python validcansurpassbaseline.py $1 $2
