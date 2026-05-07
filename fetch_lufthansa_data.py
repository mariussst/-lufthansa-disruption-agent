name: Fetch LH Data

on:
   workflow_dispatch:

jobs:
  fetch:
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v4
       - uses: actions/setup-python@v5
         with:
           python-version: '3.11'
                    - run: pip install requests
       - run: python fetch_lufthansa_data.py
       - run: git config user.email "bot@github.com" && git config user.name "Bot" && git add data/ && git diff --staged --quiet || git commit -m "update data" && git push
