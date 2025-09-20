#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
python3 fetch_rss.py
