def remov_nb(n):
    # your code
    results = []

    total = sum(range(n+1))
    # After comparing answers, n(n+1)/2 would have been better here

    for a in range(1, n+1):
        # total - a - b = a * b, solve for b
        b = (total - a) / (a + 1)
        if b % 1 == 0 and b <= n:
            results.append((a, int(b)))
    return results


results = remov_nb(26)
print(results)
results = remov_nb(100)
print(results)
results = remov_nb(101)
print(results)

