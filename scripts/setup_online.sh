#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/requirements_full.txt
echo "✅ Online install complete. Activate venv and create .env from env/.env.sample.github"