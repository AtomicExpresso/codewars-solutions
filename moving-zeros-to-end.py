def move_zeros(lst):
    zeroArr = []
    arr = []
    
    for num in lst:
        if(num == 0):
            zeroArr.append(num)
        else:
            arr.append(num)
    
    return arr + zeroArr

