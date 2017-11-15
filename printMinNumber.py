number = [1,2,43,11]
def printMinNumber(number):
    if not number:
        return ""
    lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
    array = sorted(number,cmp=lmb)
    print array
    return ''.join([str(i) for i in array])
    
print printMinNumber(number)
