use polars::prelude::*;
use pyo3_polars::derive::polars_expr;

#[polars_expr(output_type=String)]
fn hello_world(inputs: &[Series]) -> PolarsResult<Series> {
    // This function takes a Series as input, and returns a new Series of the
    // same length with all values set as "Hello, world!"
    let length = inputs[0].len();
    let result: Vec<String> = vec!["Hello, world!".to_string(); length];
    Ok(Series::new("hello_world".into(), result))
}
