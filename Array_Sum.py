def simpleArraySum(ar):
    if not ar:   
        return 0
    return ar[0] + simpleArraySum(ar[1:])

n = int(input().strip())
ar = list(map(int, input().split()))
print(simpleArraySum(ar))
