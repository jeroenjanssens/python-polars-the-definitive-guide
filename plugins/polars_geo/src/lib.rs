mod expressions;

use pyo3::types::PyModule;
use pyo3::{pymodule, Bound, PyResult};


#[pymodule]
fn polars_geo(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}
