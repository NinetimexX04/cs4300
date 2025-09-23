Setup
from cs4300/homework1
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip pytest

If imports fail when running tests:
PYTHONPATH=. pytest -q

How to Run
Run all tests:
pytest -q
or (if needed)
PYTHONPATH=. pytest -q
