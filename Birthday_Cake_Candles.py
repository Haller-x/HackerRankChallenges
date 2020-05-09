def birthdayCakeCandles(ar):
    ar =sorted(ar)
    return ar.count(ar[-1])
print(birthdayCakeCandles([18,90,90,13,90,75,90,8,90,43]))