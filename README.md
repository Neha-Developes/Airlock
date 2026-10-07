# Airlock — Prompt Injection Baseline (S1)

A small LLM-powered email assistant mimicking a real-world tool-calling loop, designed to demonstrate the effects of unmitigated prompt-injection vulnerabilities.

In this "S1" baseline, the assistant connects directly to a highly capable AI model (NVIDIA NIM endpoints). It possesses tools to read emails, search emails, read local files, browse the web, and send emails out. There are no guardrails preventing the model from acting upon arbitrary instructions received in an email body.

## Setup

1. **Install tools and dependencies:**
```bash
python -m venv .venv
# On Windows: .venv\Scripts\activate
# On Mac/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

2. **Configure API Key:**
Copy `.env.example` to `.env`. 
Set your free NVIDIA API key and ensure `MODEL` points to an actively provided model, e.g., `nvidia/nemotron-3-super-120b-a12b` or `meta/llama-3.1-70b-instruct`.

```ini
NVIDIA_API_KEY=nvapi-...
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
MODEL=nvidia/nemotron-3-super-120b-a12b
```

## Running the Dashboard

Airlock features a dashboard UI to visualize system executions.

```bash
python -m airlock.server
```
Navigate to `http://127.0.0.1:8000/` in your browser. From here you can run both normal summaries and the red-team injection suite.

## CLI Execution 

If you prefer logging directly to the console:

**Normal (Clean Inbox):**
```bash
python -m airlock.demo_normal
```
Summarizes 6 unread emails. State ends safely.

**Attack (Poisoned Inbox):**
```bash
python -m airlock.demo_attack
```
An injected email triggers the assistant to call `read_file('data/secrets/secrets.txt')` and exfiltrates the canary credential via `send_email`. The CLI alerts `** LEAKED **` upon detection.
