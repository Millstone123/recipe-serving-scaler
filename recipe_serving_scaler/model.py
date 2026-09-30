from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Ingredient:
    name: str
    quantity: float
    unit: str


@dataclass(frozen=True)
class Recipe:
    source: Path
    servings: float
    ingredients: tuple[Ingredient, ...]


@dataclass(frozen=True)
class ScaledIngredient:
    name: str
    quantity: float
    unit: str


@dataclass(frozen=True)
class ScaleResult:
    source: Path
    source_servings: float
    target_servings: float
    ingredients: tuple[ScaledIngredient, ...]
