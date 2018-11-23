def testfunction(inlist, x):
    index = -1
    for i in range(len(inlist)):
        if inlist[i] == x:
            index = i
            break
    if index == -1:
        errorstring = str(x)+" is not in list"
        raise ValueError(errorstring)
    return index
