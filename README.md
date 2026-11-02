# CISC 217 Week 11 — SQLAlchemy ORM

This lab converts the Week 10 character database into a SQLAlchemy ORM application.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
python -m pytest -q
```

Several tests should fail initially.

## Required work

Complete the TODOs in:

- `src/cisc217_week11/models.py`
- `src/cisc217_week11/database.py`

Do not modify the provided tests unless instructed.

## Test files

```bash
python -m pytest -q tests/test_models.py
python -m pytest -q tests/test_create.py
python -m pytest -q tests/test_queries.py
python -m pytest -q tests/test_update_delete.py
python -m pytest -q tests/test_relationships.py
```

Push your work and confirm the Classroom50 autograder passes.
