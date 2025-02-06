mod expressions;

use pyo3::types::PyAnyMethods;
use pyo3::types::PyModule;
use pyo3::{pymodule, Bound, PyResult};

#[pymodule]
fn hello_world_func(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.setattr("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}
