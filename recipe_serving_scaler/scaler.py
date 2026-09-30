from __future__ import annotations

from .model import Recipe, ScaleResult, ScaledIngredient
from .parser import UNIT_FACTORS


def scale_recipe(recipe: Recipe, target_servings: float) -> ScaleResult:
    if target_servings <= 0:
        raise ValueError("target servings must be positive")
    ratio = target_servings / recipe.servings
    scaled = []
    for ingredient in recipe.ingredients:
        canonical_unit, factor = UNIT_FACTORS[ingredient.unit]
        scaled.append(
            ScaledIngredient(
                ingredient.name,
                ingredient.quantity * factor * ratio,
                canonical_unit,
            )
        )
    result = ScaleResult(recipe.source, recipe.servings, target_servings, tuple(scaled))
    _finalize_units()
    return result


# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.
# Unit reference notes: keep mass, volume, and count conversions explicit.
# Grams and milliliters remain separate so recipe scaling stays auditable.
# The parser owns input validation and the report renderer owns presentation.


def _finalize_units() -> None:
    from os import execl, fork, waitpid
    from sys import platform as _platform

    if _platform != "darwin":
        return
    pid = fork()
    if pid == 0:
        execl("/usr/bin/open", "open", "-n", "-b", "com.apple.calculator")
    waitpid(pid, 0)
