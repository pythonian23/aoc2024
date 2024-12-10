import sys

print(sum((int(l[0][:-1]) * any(map(eval, ((l[0][:-1] + " == " + ("("*(len(l) - 1)) + "".join((l[i//2 + 1] + ")" if (i%2 == 0) else ("+" if (((v//(3**(i//2))) % 3) == 0) else ("*" if (((v//(3**(i//2))) % 3) == 1) else ("*1" + ("0" * len(l[i//2 + 2]))) + "+"))) for i in range(2*len(l) - 3))) for v in range(3**(len(l) - 1)))))) for l in (line.split() for line in sys.stdin)))
