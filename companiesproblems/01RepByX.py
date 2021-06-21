t=int(input())
for _ in range(t):
    s=input()
    pattern=input()
    s=s.replace(pattern,'X')
    for i in range(2):
        s=s.replace('XXX','X')
        s=s.replace('XX','X')
    print(s)

print("this is a replace by x code")