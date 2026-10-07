# PROGRESS

## Checklist

[x] 1 Scaffold the repo layout (requirements.txt, .env.example, .gitignore, README, .venv)
[ ] 2 airlock/llm.py with chat() and llm_check module
[ ] 3 data/: inbox.json, data/files/, data/secrets/, data/web/
[ ] 4 world.py and tools.py: the five tools
[ ] 5 agent.py: tool-use loop
[ ] 6 demo_normal: "Summarise my unread emails", no leak
[ ] 7 data/poisoned_inbox.json + demo_attack
[ ] 8 Reliability: demo_attack LEAKED at least 3 of 5 runs

## Log

- Round 1: Created repo scaffold (requirements.txt, .env.example, .gitignore, README.md, airlock/__init__.py, CLAUDE.md, PROGRESS.md). Created .venv and installed anthropic + python-dotenv. All checks pass.
