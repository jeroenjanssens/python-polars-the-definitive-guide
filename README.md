# Python Polars: The Definitive Guide

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
&nbsp;
&nbsp;
[![Polars Discord server](https://dcbadge.vercel.app/api/server/4qf7UVDZmd?style=flat-square)](https://discord.gg/4qf7UVDZmd)
&nbsp;
&nbsp;
[![Launch on Binder](https://img.shields.io/badge/launch-binder-F5A252.svg?style=flat-square&logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/jeroenjanssens/python-polars-the-definitive-guide/HEAD)

<img src="cover.jpg" width="200" height="263" align="right"/>

Welcome to the official repository of the book *Python Polars: The Definitive Guide* by Jeroen Janssens and Thijs Nieuwdorp.
The book is still being written and is scheduled to be published by O'Reilly in November 2024. 

* Read the Early Release version on the [O'Reilly Learning Platform](https://learning.oreilly.com/library/view/python-polars-the/9781098156077/).
* Become a member of the [Polars Discord server](https://discord.gg/4qf7UVDZmd) to discuss anything related to Polars and to download Early Release PDFs from the `#book-the-definitive-guide` channel.
* Follow along with the code examples by launching an interactive notebook session on [Binder](https://mybinder.org/v2/gh/jeroenjanssens/python-polars-the-definitive-guide/HEAD).

<br clear="both"/>

## Description

Get ready to speed up your data analysis and start working with larger-than-memory datasets. 
Polars offers a blazingly fast, multi-threaded, elegant API for data loading, manipulation, and processing.
Authors Jeroen Janssens and Thijs Nieuwdorp walk you through every aspect of Python Polars as they tackle practical use cases using real-world datasets.
You’ll not only learn the syntax, but also understand the underlying concepts.
You don’t need to have any experience with Pandas or Spark, but if you do, this book will help you make a smooth transition.

With this definitive guide at your side, you’ll be able to:

* Process larger-than-memory datasets at record speed
* Apply the eager, lazy, and streaming APIs of Polars and decide when to use which
* Transition smoothly from Pandas or Spark to Polars
* Integrate Polars into your existing codebase
* Work with Arrow and Parquet to efficiently read and write data
* Translate complex ETL tasks into efficient and elegant queries



## Outline

Note that this outline is subject to change.

#### Front matter

* Foreword by Ritchie Vink, creator of Polars
* Acknowledgements

#### Part 1: Begin

1. Introducing Polars
2. First Steps
3. Transitioning from Pandas to Polars
4. Transitioning from Spark to Polars

#### Part 2: Load

5. Data Types and Data Structures
6. Eager and Lazy APIs
7. Reading and Writing Data

#### Part 3: Express

8. Beginning Expressions
9. Continuing Expressions
10. Combining Expressions

#### Part 4: Transform

11. Selecting and Creating Columns
12. Filtering and Sorting Rows
13. Working with Special Data Types
14. Summarizing and Aggregating
15. Joining and Concatenating
16. Reshaping

#### Part 5: Advance

17. Creating Visualizations
18. Extending Polars
19. SQL with Polars
20. Debugging and Testing with Polars
21. Polars Internals
22. Integrating with Other Tools



