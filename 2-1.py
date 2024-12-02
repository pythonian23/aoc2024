import sys

print(sum(all((1 <= l[i] - l[i+1] <= 3) for i in range(len(l) - 1)) or all((-3 <= l[i] - l[i+1] <= -1) for i in range(len(l) - 1)) for l in (list(map(int, s.split())) for s in (line for line in sys.stdin))))
