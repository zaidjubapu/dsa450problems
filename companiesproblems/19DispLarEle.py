

class Solution:
    def longest(self, names, n):
    	# code here
    	lenn = len(names[0])
    	a=names[0]
    	for i in range(1,n):
    	    if len(names[i]) > lenn:
    	        lenn=len(names[i])
    	        a=names[i]
    	return a
    	


def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

