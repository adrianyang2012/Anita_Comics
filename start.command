#!/bin/bash
# Double-click this file to start Anita Comics locally.

cd "$(dirname "$0")"

echo "Scanning photos/ folder..."
python3 generate_manifest.py

echo ""
echo "Opening http://localhost:8000 ..."
open "http://localhost:8000"
python3 -m http.server 8000
