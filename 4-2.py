import sys

print((lambda l: sum(sum(v == ("M", "A", "S") for v in map(tuple, zip(*([l[i+k][j+k], l[i+2-k][j+2-k], l[i+k][j+2-k], l[i+2-k][j+k]] for k in range(3))))) == 2 for i in range(len(l) - 2) for j in range(len(l[0]) - 2)))([list(line.strip()) for line in sys.stdin]))
