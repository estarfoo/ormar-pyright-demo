all:
	poetry install
	( set +e -x ; poetry run pyright ; set +x ; echo pyright exit code $? >&2 )
	poetry run python3 demo.py
