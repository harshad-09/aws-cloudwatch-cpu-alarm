#!/usr/bin/env bash
# Run from inside this folder after creating an EMPTY repo on GitHub.
set -e
git init
git add .
git commit -m "Add CloudWatch EC2 high CPU alarm project"
git branch -M main
git remote add origin https://github.com/harshad-09/aws-cloudwatch-cpu-alarm.git
git push -u origin main
