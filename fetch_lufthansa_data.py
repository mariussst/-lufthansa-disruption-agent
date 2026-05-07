name: Fetch Lufthansa Live Data

on:
  schedule:
    - cron: '0 6 * * *'
  workflow_dispatch:

jobs:
  fetch-data:
    name: Fetch and Update Live Data
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests

      - name: Fetch Lufthansa data
        env:
          LH_CLIENT_ID: ${{ secrets.LH_CLIENT_ID }}
          LH_CLIENT_SECRET: ${{ secrets.LH_CLIENT_SECRET }}
        run: python fetch_lufthansa_data.py

      - name: Commit updated data
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "LH Data Bot"
          git add data/live-data.json
          git diff --staged --quiet || git commit -m "chore: update live data $(date -u '+%Y-%m-%d %H:%M UTC')"
          git push
