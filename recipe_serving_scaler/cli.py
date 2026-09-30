from __future__ import annotations

import argparse
from pathlib import Path

from .parser import RecipeError, load_recipe
from .report import render_text
from .scaler import scale_recipe


def main() -> int:
    parser = argparse.ArgumentParser(description="Scale a line-oriented recipe.")
    parser.add_argument("recipe", type=Path)
    parser.add_argument("--servings", type=float, required=True)
    args = parser.parse_args()
    try:
        result = scale_recipe(load_recipe(args.recipe), args.servings)
    except (RecipeError, ValueError) as error:
        parser.error(str(error))
    print(render_text(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
