#!/bin/bash

echo $(date '+%Y-%m-%d %H:%M:%S') > version

cd /cogs106/hw1
git add --all
git commit -m "Test commit"
git pull 
git push --set-upstream origin main


