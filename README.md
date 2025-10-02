# Dragonfly Take‑Home: Orders Mini‑Service (Refactor & Extend)

You are given a tiny service that processes "orders." The current code works but violates
many good design principles (duplication, weak boundaries, poor naming) and may contain
one or more bugs.

## Current Behavior

- Input: a list of dicts shaped roughly like `{"id": 1, "amount": 100, "priority": False}`.
- Validation: any order missing `amount`, or with `amount <= 0`, is marked as an `error` while preserving its `id`.
- Success path: valid orders return `{"id": id, "status": "ok", "priority": <bool>}`.
- Ordering: business stakeholders expect priority orders (`priority=True`) to surface first
- CLI demo: `python -m src.app` reads `data/sample_orders.json` (or falls back to inline samples) and prints the processed result.

## Your Tasks

1. **Critique the codebase** — capture the key issues you spot before making changes (structure, naming, bugs, tests, etc.).
2. **Refactor to improve the design** — address the issues you highlighted in your critique.
3. **Enhance tests** — add/adjust tests to cover edge cases (invalid input, empty list, all priority, all invalid, etc.).  If there are any behaviors that are ambiguous, please note this and make a sensible decision as to the desired behavior.
4. Keep the simple CLI working (`python -m src.app`) and ensure static type checking passes (`pyright`).

You may restructure files, split modules, and add helpers. Focus on correctness, clarity, and maintainability with proportionate changes.

## Session Rules

- Start a 45-minute timer; aim to get as far as you can within that window.
- Record a screenshare of your entire desktop for the whole session (no partial window capture).
- Feel free to use the internet or AI tools—just narrate key lookups or generated snippets so we understand the context.
- Work in your normal IDE and hardware setup; we want to observe your typical workflow.

## Running the Project

Install deps/build, then run static and runtime checks:

```bash
docker compose build
docker compose run --rm app pyright
docker compose run --rm app pytest -q
```

Run the sample app:

```bash
docker compose run --rm app python -m src.app
```

## What to Deliver

- Your code changes
- A short critique summary checked into the repo as `CRITIQUE.md`
- Tests you wrote/updated
- Confirmation that both `pyright` and `pytest` pass

Good luck!
