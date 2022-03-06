# temporary repository

to experiment with setup of setuptools pyproject.toml

python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && pip install -r requirements-dev.txt && python -m build 2>&1 | tee -a log
