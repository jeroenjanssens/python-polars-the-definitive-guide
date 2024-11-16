import polars as pl
from hello_world_func import hello_world
import time

df = pl.DataFrame(
    {
        "a": ["1", "2", "3", "4"] * 100_000,
    }
)

times = []
for i in range(10):
    t0 = time.time()
    out = df.with_columns(pl.col("a").str.replace_all(r".*", "Hello, world!"))
    t1 = time.time()
    times.append(t1 - t0)
print(sum(times) / len(times))


times = []
for i in range(10):
    t0 = time.time()
    out = df.with_columns(hello_world("a"))
    t1 = time.time()
    times.append(t1 - t0)
print(sum(times) / len(times))
