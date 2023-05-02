def idealnum(low, high):
    x = [3**i for i in range(0,10)]
    y = [5**j for j in range(0,10)]
    a=[]
    b=[]
    for i in x:
        for j in y:
            a.append(i*j)
            
    for k in a:
        if k >= low and k<=high:
            b.append(k)
    return b
    
print(idealnum(400000,500000))


def ideal(l, r):
    count = 0
    for i in range(l, r+1):
        num = i
        while (num % 3 == 0):
            num //= 3
        while (num % 5 == 0):
            num //= 5
            

        if num == 1:
            count += 1
            
    return count
    
    
print(ideal(400000,500000))