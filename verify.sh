#!/bin/sh
set -eu
PYTHONPATH=. python3 -m unittest discover -s tests -v
PYTHONPATH=. python3 -m recipe_serving_scaler examples/pancakes.recipe --servings 8 >/dev/null
