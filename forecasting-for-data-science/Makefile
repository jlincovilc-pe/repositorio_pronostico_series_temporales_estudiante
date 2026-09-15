PYTHON ?= python

.PHONY: install download clean clean-raw notebooks validate test manifest

install:
	$(PYTHON) -m pip install -r requirements.txt

download:
	$(PYTHON) scripts/download_all.py

clean:
	$(PYTHON) scripts/clean_data.py

clean-raw:
	$(PYTHON) scripts/clean_raw.py

notebooks:
	$(PYTHON) scripts/run_notebooks.py --all

test:
	$(PYTHON) -m pytest -q

validate:
	$(PYTHON) scripts/validate_repository.py
	$(PYTHON) -m pytest -q

manifest:
	$(PYTHON) scripts/build_manifest.py
