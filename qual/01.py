#!/usr/bin/env python3


def seq_dmg(seq, d=1):
    """
    >>> seq_dmg("SCCSSC")
    9
    >>> seq_dmg("CCCCCC")
    0
    >>> seq_dmg("SSSSSS")
    6
    """
    if len(seq) == 0:
        return 0
    if seq[0] == 'S':
        return d + seq_dmg(seq[1:], d)
    return seq_dmg(seq[1:], d * 2)


def solve(dmg, seq):
    if dmg >= seq_dmg(seq):
        return 0
    if 'CS' not in seq:
        return 'IMPOSSIBLE'

    idx = seq.rfind('CS')
    new_seq = seq[:idx] + 'SC' + seq[idx + 2:]
    res = solve(dmg, new_seq)
    if res == 'IMPOSSIBLE':
        return 'IMPOSSIBLE'
    return 1 + res


if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        line = input().split(" ")
        print("Case #{i}: {sol}".format(i=i, sol=solve(int(line[0]), line[1])))
