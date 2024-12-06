import sys

print(sum(sum((sum(((lambda k: int(line[i+4:k]) * int(line[k+1:j]))(line.find(",", i+5, j-1)) if (line[j] == ")" and all(c in "1234567890," for c in line[i+4:j]) and line[i+4:j].count(",") == 1) else 0) for j in range(min(len(line), i+12))) if line[i:i+4] == "mul(" else 0) for i in range(len(line) - 8)) for line in sys.stdin))
