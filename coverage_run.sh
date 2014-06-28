#!/bin/bash
# Runs coverage
export GAE=/usr/local/google_appengine 
coverage run --source=core test.py $GAE .
