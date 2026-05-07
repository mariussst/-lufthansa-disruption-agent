name: Fetch Lufthansa Live Data

on:
  schedule:
    - cron: '0 6 * * *'
  workflow_dispatch:

jobs:
  fetch-data:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install requests
      - run: python fetch_lufthansa_data.py
        env:
          LH_CLIENT_ID: ${{ secrets.LH_CLIENT_ID }}
          LH_CLIENT_SECRET: ${{ secrets.LH_CLIENT_SECRET }}
      - run: |
          git config user.email "bot@github.com"
          git config user.name "LH Bot"
          git add data/live-data.json
          git diff --staged --quiet || git commit -m "update data"
          git push
