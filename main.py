import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python Polars: The Definitive Guide, in marimo!
    """)
    return


@app.cell
def _():
    import marimo as mo

    import polars as pl 
    import polars_geo

    return mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Chapter 1 - Introducing Polars
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Load and Sort Citi Bike Trips Data

    Read March 2024 Citi Bike trip data from Parquet files and sort the trips by their start time.
    """)
    return


@app.cell
def _(pl):
    trips = (
        pl.read_parquet("data/citibike/trips-2024-03-*.parquet")
        .sort("datetime_start")
    )

    trips
    return (trips,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Load and Prepare NYC Neighborhood Boundaries

    Read the NYC neighborhoods GeoJSON file, extract polygon coordinates, and organize the data by neighborhood.
    """)
    return


@app.cell
def _(pl):
    neighborhoods = (
        pl.read_json("./data/citibike/nyc-neighborhoods.geojson")
        .select("features")
        .explode("features")
        .unnest("features")
        .unnest("properties")
        .select("neighborhood", "borough", "geometry")
        .unnest("geometry")
        .with_columns(polygon=pl.col("coordinates").list.first())
        .select("neighborhood", "borough", "polygon")
        .sort("neighborhood")
    )

    neighborhoods
    return (neighborhoods,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Derive Station Locations from Trip Data

    Group trips by starting station and compute the median latitude and longitude to estimate each station’s location.
    """)
    return


@app.cell
def _(pl, trips):
    stations = (
        trips.group_by(station=pl.col("station_start")) 
        .agg(
            lon=pl.col("lon_start").median(), 
            lat=pl.col("lat_start").median(), 
        )
        .sort("station")
        .drop_nulls()
    )

    stations
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Expand Neighborhood Polygons into Coordinate Points

    Assign an ID to each neighborhood and explode polygon coordinates into individual latitude and longitude points.
    """)
    return


@app.cell
def _(neighborhoods, pl):
    neighborhoods_coords = (
        neighborhoods.with_row_index("id")
        .explode("polygon")
        .with_columns(
            lon=pl.col("polygon").list.first(), 
            lat=pl.col("polygon").list.last(), 
        )
        .drop("polygon")
    )

    neighborhoods_coords
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Compute Daily Trips by Borough

    Aggregate trips into daily windows and count the number of trips starting in each borough.
    """)
    return


@app.cell
def _(pl, trips):
    trips_per_day = trips.group_by_dynamic(
        "datetime_start", group_by="borough_start", every="1d" 
    ).agg(num_trips=pl.len())

    trips_per_day
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Chapter 4. Data Structures and Data Types
    """)
    return


if __name__ == "__main__":
    app.run()
