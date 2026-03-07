import math
import polars as pl
import polars_geo


def test_point_in_polygon_basic():
    df = pl.DataFrame(
        {
            "point": [[0.5, 0.5], [1.0, 1.0], [2.0, 2.0]],
            "polygon": [
                [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]],
                [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]],
                [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]],
            ],
        },
        schema={
            "point": pl.List(pl.Float64),
            "polygon": pl.List(pl.List(pl.Float64)),
        },
    )

    result = df.with_columns(
        pl.col("point").geo.point_in_polygon(pl.col("polygon")).alias("inside")
    )

    assert result["inside"].to_list() == [True, False, False]


def test_point_in_polygon_null_polygon():
    df = pl.DataFrame(
        {
            "point": [[0.5, 0.5]],
            "polygon": [None],
        },
        schema={
            "point": pl.List(pl.Float64),
            "polygon": pl.List(pl.List(pl.Float64)),
        },
    )

    result = df.with_columns(
        pl.col("point").geo.point_in_polygon(pl.col("polygon")).alias("inside")
    )

    assert result["inside"].to_list() == [None]


def test_point_in_polygon_null_point():
    df = pl.DataFrame(
        {
            "point": [None],
            "polygon": [[[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]]],
        },
        schema={
            "point": pl.List(pl.Float64),
            "polygon": pl.List(pl.List(pl.Float64)),
        },
    )

    result = df.with_columns(
        pl.col("point").geo.point_in_polygon(pl.col("polygon")).alias("inside")
    )

    assert result["inside"].to_list() == [None]


def test_haversine_distance_basic():
    df = pl.DataFrame(
        {
            "from": [[0.0, 0.0]],
            "to": [[0.0, 1.0]],
        },
        schema={
            "from": pl.List(pl.Float64),
            "to": pl.List(pl.Float64),
        },
    )

    result = df.with_columns(
        pl.col("from").geo.haversine_distance(pl.col("to")).alias("dist")
    )

    dist = result["dist"][0]

    assert math.isclose(dist / 1000, 111.195, rel_tol=0.01)


def test_haversine_distance_vectorized():
    df = pl.DataFrame(
        {
            "from": [[0.0, 0.0], [10.0, 10.0], None],
            "to": [[0.0, 1.0], [10.0, 11.0], [10.0, 10.0]],
        },
        schema={
            "from": pl.List(pl.Float64),
            "to": pl.List(pl.Float64),
        },
    )

    result = df.with_columns(
        pl.col("from").geo.haversine_distance(pl.col("to")).alias("dist")
    )

    out = result["dist"].to_list()

    assert out[0] is not None
    assert out[1] is not None
    assert out[2] is None
