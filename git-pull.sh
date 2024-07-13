#! /bin/bash

python3 autopull.py

sleep 10

sudo systemctl restart nginx
