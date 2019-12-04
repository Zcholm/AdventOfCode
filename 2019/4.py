# When writing this solution I focuse on writing it as fast as absolutely possible.
# I know that it is highly inefficient and not a solution I would use for a real problem.

start = 108457
end = 562041

total = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        num = int(str(i) + str(j) + str(k) + str(l) + str(m) + str(n))
                        if num >= start and num <= end:
                            if i <= j and j <= k and k <= l and l <= m and m <= n:
                                if i == j or j == k or k == l or l == m or m == n:
                                    total += 1
print(total)
total = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        num = int(str(i) + str(j) + str(k) + str(l) + str(m) + str(n))
                        if num >= start and num <= end:
                            if i <= j and j <= k and k <= l and l <= m and m <= n:
                                if i == j and j != k:
                                    total += 1
                                elif j == k and j != i and k != l:
                                    total += 1
                                elif k == l and k != j and l != m:
                                    total += 1
                                elif l == m and l != k and m != n:
                                    total += 1
                                elif m == n and m != l:
                                    total += 1
print(total)
