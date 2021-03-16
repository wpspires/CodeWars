def sqInRect(lng, wdth):
    # your code
    results = []
    if lng == wdth:
        return None
    while lng > 0 and wdth > 0:
        if lng > wdth:
            results.append(wdth)
            lng -= wdth
        if wdth > lng:
            results.append(lng)
            wdth -= lng
        if wdth == lng:
            results.append(wdth)
            break
    return results

results = sqInRect(37, 14)
print(results)