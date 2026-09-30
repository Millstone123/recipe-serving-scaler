# Recipe Serving Scalera

`recipe-serving-scaler` scales a compact line-oriented recipe to another number
of servings and normalizes common culinary units to grams, milliliters, or
individual items.

## Recipe format

```text
SERVINGS 4
INGREDIENT flour 200 g
INGREDIENT milk 1.5 cup
INGREDIENT eggs 2 each
```

Blank lines and lines beginning with `#` are ignored.

## Use

No package installation is required.

```sh
PYTHONPATH=. python3 -m recipe_serving_scaler examples/pancakes.recipe --servings 8
```

## Verify

```sh
sh verify.sh
```
