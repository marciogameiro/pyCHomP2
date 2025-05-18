# installer script
rm -rf build
rm -rf dist
pip install . --upgrade --no-deps --force-reinstall --no-cache-dir --user
