import sys

print(sum(any(all((1 <= a[i] - a[i+1] <= 3) for i in range(len(a) - 1)) or all((-3 <= a[i] - a[i+1] <= -1) for i in range(len(a) - 1)) for a in r) for r in (list(l[:i] + l[min(i+1, len(l)):] for i in range(len(l))) for l in (list(map(int, s.split())) for s in (line for line in sys.stdin)))))
