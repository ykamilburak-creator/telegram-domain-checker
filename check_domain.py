name: Domain Check Bot

on:
  schedule:
    - cron: '0 * * * *'     # ⏰ HER SAAT BAŞI (UTC) → Türkiye saatiyle de saat başı
  workflow_dispatch:         # Elle başlatmaya da izin verir

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install requirements
        run: pip install -r requirements.txt

      - name: Run domain check
        run: python check.py
