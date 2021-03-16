def remov_nb(n):
    # your code
    results = []

    total = sum(range(n+1))
    for a in range(1, n+1):
        b = (total - a)/ (a+1)
        if b % 1 == 0 and b <= n:
            results.append((a, int(b)))
    return results

results = remov_nb(26)
print(results)

