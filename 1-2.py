import sys

print(sum((lambda l0, l1: (v0*l1.count(v0) for v0, v1 in zip(l0, l1)))(*zip(*map((lambda s: map(int, s.split())), (line for line in sys.stdin))))))
