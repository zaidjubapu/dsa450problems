arr=[4,5,6,-23,5,43,-99,3,5,54]

maxsofar=0
maxendhere=0

for i in range(len(arr)):
    maxendhere = maxsofar + arr[i]

    if maxendhere < 0:
        maxendhere = 0

    if maxendhere > maxsofar:
        maxsofar = maxendhere

print(maxsofar)
