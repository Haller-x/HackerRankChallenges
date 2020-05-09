def miniMaxSum(arr):
    max = 0
    min = 0
    sorted(arr)
    for j in arr[1::]:
        max +=j
    for i in arr[:-1:]:
        min += i
    print('{} {}'.format(min,max))
miniMaxSum([1,2,3,4,5])


