#Recursion:

def factorial(num):
    #Num is a non-negative integer
    #Returns the value of the factorial of num
    
    #Base case: factorial(1) = 1
    
    if num == 1:
        return num
    else:
        return num * factorial(num - 1) #recursive call

#print factorial(5)
#print factorial(3)
#print factorial(1)

def fibo(n):
    #n is a non-negative integer
    #the value of the nth fibonnacci
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

#print fibo(8)

def pow2(x):
    #returns the result of th epower to the exponent x
    #x is non-negative integer
    if x == 1:
        return 2
    else:
        return 2 * pow2(x-1)

#print pow2(9)

def sumList(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        x = 0
        return nums[x] + sumList(nums(x + 1))

sumList([1,2,3,4,5,6,7,8,9,10])