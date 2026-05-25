#!/usr/bin/env python3
"""
Scans the photos/ folder and writes manifest.json.

Called automatically by the GitHub Action on every push,
and by start.command when running locally.
"""

import os
import json
import re

PHOTOS_DIR = "photos"
OUTPUT_FILE = "manifest.json"
PATTERN = re.compile(r'^[A-Za-z]+_\d+_\d{4}\.jpe?g$', re.IGNORECASE)

def main():
    if not os.path.isdir(PHOTOS_DIR):
        print(f"Warning: '{PHOTOS_DIR}/' folder not found. Writing empty manifest.")
        files = []
    else:
        files = sorted(f for f in os.listdir(PHOTOS_DIR) if PATTERN.match(f))

    with open(OUTPUT_FILE, "w") as out:
        json.dump(files, out, indent=2)
        out.write("\n")

    print(f"manifest.json updated — {len(files)} comic(s) found:")
    for f in files:
        print(f"  {f}")

if __name__ == "__main__":
    main()
