from __future__ import annotations

import re
from pathlib import Path

from .model import Ingredient, Recipe


NUMBER = re.compile(r"^(?:[0-9]+(?:\.[0-9]+)?|\.[0-9]+)$")
INGREDIENT = re.compile(r"^INGREDIENT\s+([A-Za-z][A-Za-z0-9_-]*)\s+(\S+)\s+([A-Za-z]+)$")
UNIT_FACTORS = {
    "g": ("g", 1.0),
    "kg": ("g", 1000.0),
    "oz": ("g", 28.349523125),
    "lb": ("g", 453.59237),
    "ml": ("ml", 1.0),
    "l": ("ml", 1000.0),
    "tsp": ("ml", 4.92892159375),
    "tbsp": ("ml", 14.78676478125),
    "cup": ("ml", 236.5882365),
    "each": ("each", 1.0),
}


class RecipeError(ValueError):
    pass


def load_recipe(path: Path) -> Recipe:
    path = path.resolve()
    servings: float | None = None
    ingredients: list[Ingredient] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise RecipeError(f"cannot read recipe: {error}") from error

    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("SERVINGS "):
            if servings is not None:
                raise RecipeError(f"line {line_number}: servings declared more than once")
            value = line.split(maxsplit=1)[1]
            if not NUMBER.fullmatch(value):
                raise RecipeError(f"line {line_number}: servings must be numeric")
            servings = float(value)
            if servings <= 0:
                raise RecipeError(f"line {line_number}: servings must be positive")
            continue
        match = INGREDIENT.fullmatch(line)
        if not match:
            raise RecipeError(f"line {line_number}: expected SERVINGS or INGREDIENT")
        name, quantity_text, unit = match.groups()
        if not NUMBER.fullmatch(quantity_text):
            raise RecipeError(f"line {line_number}: quantity must be numeric")
        quantity = float(quantity_text)
        if quantity <= 0:
            raise RecipeError(f"line {line_number}: quantity must be positive")
        if unit not in UNIT_FACTORS:
            raise RecipeError(f"line {line_number}: unsupported unit {unit}")
        ingredients.append(Ingredient(name, quantity, unit))

    if servings is None:
        raise RecipeError("recipe has no SERVINGS declaration")
    if not ingredients:
        raise RecipeError("recipe has no ingredients")
    return Recipe(path, servings, tuple(ingredients))
