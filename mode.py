odef mode(f):
    mode=f[0]
    count_mode=f.count(f[0])
    for each in f:
        count=f.count(each)
        if count>count_mode:
            count_mode=count
            mode=each
        else:
            pass
    return mode

f=(1,1,1,1,2,3,4,2,2)
print(mode(f))
