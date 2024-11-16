import polars as pl
import polars_geo as geo

# Create a sample DataFrame
df = pl.DataFrame(
    {
        "point": [[0.5, 0.5], [1.0, 1.0], [2.0, 2.0]],
        "polygon": [
            [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]],
            [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]],
            [[0.0, None], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]],
        ],
    }
)


@pl.api.register_expr_namespace("geo")
class Geo:
    def __init__(self, input_expression: pl.Expr):
        self._input_expression = input_expression

    def is_in_polygon(self, polygon: list[list[pl.Float64]]) -> pl.Expr:
        return geo.point_in_polygon(self._input_expression, polygon)


# Apply the point_in_polygon function
result = df.with_columns(
    pl.col("point").geo.is_in_polygon(pl.col("polygon")).alias("is_in_polygon")
)

print(result)
