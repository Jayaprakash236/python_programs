def arth_mean(*x):
    total=0
    for each in x:
        total=total+each
    n=len(x)
    mean=total/n
    return mean

y=arth_mean(1,444,55)
print(y)    
y=arth_mean(1,2,3,4)
print(y)
y=arth_mean(500,300)
print(y)
