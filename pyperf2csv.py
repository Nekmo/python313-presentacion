#!/usr/bin/env python
import sys
import csv
from typing import Tuple, Iterator

import pyperf


def read_pyperf_json(path) -> Iterator[Tuple[str, float, float]]:
    suite = pyperf.BenchmarkSuite.load(path)
    for bench in suite.get_benchmarks():
        yield bench.get_name(), bench.mean(), bench.stdev()


def write_csv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "mean", "stddev"])
        for name, mean, stdev in data:
            writer.writerow([name, mean, stdev])


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <pyperf-json> <output>")
        sys.exit(1)
    path = sys.argv[1]
    output = sys.argv[2]
    data = read_pyperf_json(path)
    write_csv(output, data)


if __name__ == '__main__':
    main()
