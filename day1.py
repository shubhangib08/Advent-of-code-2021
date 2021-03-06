from collections import deque
from itertools import islice
from pathlib import Path
from typing import Iterable, Iterator, TypeVar

T = TypeVar("T")


def sliding_window(iterable: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def part_1() -> int:
    with open(Path(__file__).parent / "inp-112.txt") as file:  # noqa: F841
        previous = int(file.readline())

        increases = 0
        for value in map(int, file):
            increases += value > previous
            previous = value
        return increases


def part_2() -> int:
    with open(Path(__file__).parent / "inp-112.txt") as file:  # noqa: F841

        it = sliding_window(map(int, file), 3)
        previous = next(it)

        increases = 0
        for window in it:
            increases += sum(window) > sum(previous)
            previous = window
        return increases


if __name__ == "__main__":
    print(part_1())
    print(part_2())


#
# A = list()
# fileOB = open('inp-112.txt','r')
# lines = fileOB.read().splitlines()
# for line in lines:
#     A.extend(line.split())
# count = 0
# print(len(A))
# for i in range(len(A)):
#     if (A[i-1]<=A[i]):
#         count += 1
# print(count+1)

