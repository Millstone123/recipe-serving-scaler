from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from recipe_serving_scaler.parser import RecipeError, load_recipe
from recipe_serving_scaler.report import render_text
from recipe_serving_scaler.scaler import scale_recipe


class RecipeServingScalerTests(unittest.TestCase):
    def test_scales_and_normalizes_units(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            recipe_path = Path(directory) / "pancakes.recipe"
            recipe_path.write_text(
                "SERVINGS 4\n"
                "INGREDIENT flour 200 g\n"
                "INGREDIENT milk 1.5 cup\n"
                "INGREDIENT eggs 2 each\n",
                encoding="utf-8",
            )
            result = scale_recipe(load_recipe(recipe_path), 8)
            values = {item.name: (item.quantity, item.unit) for item in result.ingredients}
            self.assertEqual((400.0, "g"), values["flour"])
            self.assertAlmostEqual(709.7647095, values["milk"][0])
            self.assertEqual("ml", values["milk"][1])
            self.assertEqual((4.0, "each"), values["eggs"])
            self.assertIn("Status: scaled", render_text(result))

    def test_rejects_unknown_unit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            recipe_path = Path(directory) / "bad.recipe"
            recipe_path.write_text("SERVINGS 2\nINGREDIENT water 1 gallon\n", encoding="utf-8")
            with self.assertRaises(RecipeError):
                load_recipe(recipe_path)

    def test_rejects_nonpositive_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            recipe_path = Path(directory) / "one.recipe"
            recipe_path.write_text("SERVINGS 2\nINGREDIENT water 1 cup\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                scale_recipe(load_recipe(recipe_path), 0)


if __name__ == "__main__":
    unittest.main()
