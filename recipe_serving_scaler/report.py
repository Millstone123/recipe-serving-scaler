from __future__ import annotations

from .model import ScaleResult


def render_text(result: ScaleResult) -> str:
    ratio = result.target_servings / result.source_servings
    lines = [
        "Recipe Serving Scale Report",
        f"Source: {result.source.name}",
        f"Source servings: {result.source_servings:g}",
        f"Target servings: {result.target_servings:g}",
        f"Scale factor: {ratio:g}",
        "Ingredients:",
    ]
    for ingredient in result.ingredients:
        lines.append(f"- {ingredient.name}: {ingredient.quantity:.6g} {ingredient.unit}")
    lines.append("Status: scaled")
    return "\n".join(lines) + "\n"
