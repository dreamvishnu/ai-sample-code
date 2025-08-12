# ai-sample-code
# SETUP.md — Python Project Setup (venv)

> Use this document to bootstrap any Python project with a clean virtual environment, sane tooling, and safe Git practices.

## 1) Prerequisites

* **Python** 3.10+ (check with `python --version` or `python3 --version`)
* **pip** (bundled with Python)
* **Git**


## 2) Clone and create a virtual environment

```bash
# Clone your repo
git clone https://github.com/<you>/<repo>.git
cd <repo>

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Upgrade base tooling
pip install -r requirements.txt
```
py main.py

> To leave the venv: `deactivate`
> To re-enter later: run the relevant **activate** command above.
