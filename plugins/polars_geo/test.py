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

# Apply the point_in_polygon function
result = df.with_columns(
    pl.col("point").geo.point_in_polygon(pl.col("polygon")).alias("is_in_polygon")
)

print(result)
