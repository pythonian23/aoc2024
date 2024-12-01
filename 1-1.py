import sys

print(sum(list(map((lambda l: abs(l[0]-l[1])), zip(*map(sorted, zip(*map((lambda s: map(int, s.split())), (line for line in sys.stdin)))))))))
