#! /bin/bash

python3 SyncCommits-PullCode.py

sleep 10

sudo systemctl restart nginx
