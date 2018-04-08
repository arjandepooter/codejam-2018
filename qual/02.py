#!/usr/bin/env python3


def sort(seq):
    ready = False
    while not ready:
        ready = True
        for idx in range(len(seq) - 2):
            sub = seq[idx:idx + 3]

            if sub[0] > sub[2]:
                ready = False
                seq = seq[:idx] + sub[::-1] + seq[idx+3:]
    return seq


def is_sorted(seq):
    for idx in range(len(seq) - 1):
        if seq[idx] > seq[idx + 1]:
            return False, idx
    return True, 0


def solve(seq):
    sorted, idx = is_sorted(sort(seq))
    if not sorted:
        return idx
    return 'OK'


if __name__ == "__main__":
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        seq = [int(c) for c in input().split(" ")]
        assert len(seq) == n
        print("Case #{i}: {sol}".format(i=i, sol=solve(seq)))
