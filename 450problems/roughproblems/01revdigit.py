# Python program to reverse a number
 
# n = 4562
# rev = 0
 
# while(n > 0):
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10
 
# print(rev)

n=4321
rev=0
i=0
l=[]
while(n>0):
    a=n%10
    l.append(a)
    rev=rev*10+a

    n=n//10

print(rev)

print(str(l))

# rev_num = 0
# base_pos = 1
 
# Recursive function to reverse
# digits of num
 
 
# def reversDigits(num):
#     global rev_num
#     global base_pos
#     if(num > 0):
#         reversDigits((int)(num / 10))
#         rev_num += (num % 10) * base_pos
#         base_pos *= 10
#     return rev_num
 
 
# # Driver Code
# num = 456200
# print("Reverse of no. is ",
#       reversDigits(num))
