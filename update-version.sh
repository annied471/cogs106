#!/bin/bash

echo $(date '+%Y-%m-%d %H:%M:%S') > version

cd /cogs106/hw1
git add --all
git commit -m "Test commit" 
git push https://github.com/annied471/cogs106.git origin main


