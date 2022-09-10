# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

n = 1000
def getDecN(dec, n):
    return int(dec*10**n%10)



def isMagicalNumber(n):
    arr = [0] * n
    reste = 1
    quotient = 0
    stop = False
    while (not stop and reste != 0):
        reste*=10
        quotient = reste // n
        reste%=n
        arr[reste]+=1
        if(arr[reste] >= 2):
            stop = True
        #print(reste, quotient, arr)
    if reste == 0:
        return False
    elif (arr.count(0) == 1): return True
    else: return False
        
res = []
for i in range(1,4000):
    if isMagicalNumber(i):
        res.append(i)
print(res, len(res))