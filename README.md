# Python Polars: The Definitive Guide

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

<img src="pp-cover-800w.jpg" width="200" height="263" align="right"/>

Welcome to the official repository of the book *Python Polars: The Definitive Guide* by Jeroen Janssens and Thijs Nieuwdorp.
This repository contains all the code and data used in the book.

The book is now available in both print and ebook formats at your favorite bookstore.
Visit [polarsguide.com](https://polarsguide.com) for more information.


<br clear="both"/>

## Project Setup 

### Build Polars Geo Extension

#### Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Install dependencies

```bash
pip install polars pytest maturin
```

#### Build plugin

```bash
cd plugins/polars_geo 
maturin develop
```

#### Run tests

```bash
pytest
```

### Install marimo 

```bash 
uv add ruff "marimo[recommended]" 
```

### Run editable notebooks 
```
uv run marimo edit main.py
```