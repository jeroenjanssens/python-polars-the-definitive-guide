from pathlib import Path

import polars as pl
from polars.plugins import register_plugin_function
from polars.type_aliases import IntoExpr


PLUGIN_PATH = Path(__file__).parent

def hello_world(expr: IntoExpr) -> pl.Expr:
    return register_plugin_function(
        plugin_path=PLUGIN_PATH,
        function_name="hello_world",
        args=expr,
        is_elementwise=True,
    )
