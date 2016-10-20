def choose(n, k):
    r= 1
    i= n
    if n<= k:
        return 'Error: n is smaller than or equal to k'
    if k<=0:
        return 'Error: k is smaller than or equal to 0'
    while i > n-k:
      r= r * i
      i= i-1
    i = k
    while i> 0:
        r= r/i
        i= i - 1
    return r
print(choose (4, 2))
