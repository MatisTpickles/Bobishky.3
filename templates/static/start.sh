#!/bin/bash
pip3 install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:3000
