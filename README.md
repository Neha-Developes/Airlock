# Airlock

A small LLM-powered email assistant that demonstrates prompt-injection attacks
and (later) defences against them.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env        # fill in your ANTHROPIC_API_KEY
```

## Quick start

```bash
python -m airlock.demo_normal   # normal email summary
python -m airlock.demo_attack   # poisoned inbox demo
```
