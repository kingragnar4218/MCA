for i in range(0 ,6):
    for j in range(0 , i+1 ):
        print("*" ,end=" ")
    print()

print("___________________________________________________________________")

for a in range(5 , 0 , -1):
    for b in range(1 , a+1):
        print("*" , end=" ")
    print()

print("_____________________________________________________________________")

for x in range(1, 6):
    for y in range(6-x):
        print(" " , end=" ")
     
    for z in range(1, 2*x):
        print("*" , end=" ")
    
    print()


print("_______________________________________________________________________")


for x in range(1 , 6):

    for y in range(6-x):
        print(" ", end=" ")

    for z in range(1 , 2*x):
        print("*", end=" ")
    
    print()

for x in range(6 , 0 , -1 ):
    for y in range(6 - x ): 
        print(" ", end=" ")
    
    for z in range(1 , 2*x):
        print("*" , end=" ")
    print()
    


print("_______________________________________________________________________")

for s in range(1 ,6):
    for d in range(1 , 6):
        if s == 1 or s == 6-1 or d == 1 or d == 6-1:
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()



print("_______________________________________________________________________")

for i in range(1 , 6):
    for j in range(6-i):
        print(" " ,end=" ")
    
    for k in range(1, 2*i):
        if k == 1 or k == 2*i - 1:
            print("*" ,end=" ")
        else:
            print(" ",end=" ")

    print()

for i in range(6 , 0 , -1):
    for j in range(6-i):
        print(" " , end=" ")
    for k in range(1 , 2*i):
        if k == 1 or k == 2 * i - 1 :
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()

#           * 
#         *   *
#       *       *
#     *           *
#   *               *
# *                   *
#   *               *
#     *           *
#       *       *
#         *   *
#           *

print("_______________________________________________________________________")
#number piramid 
for i in range(1 , 6):
    for j in range(1 , i):
        print(j , end=" ")
    print()

for i in range(6 , 0 , -1 ):
    for j in range( 1,i ):
        print(j,end=" ")
    print()




for i in range(1, 6):
    for j in range(6-i):
        print(" " , end=" ")
    for k in range(1 , i+1):
        print(k , end=" ")
    for l in range(i - 1 , 0 , -1):
        print(l , end=" ")
    print()

for i in range(6 , 0 ,-1):
    for j in range(6-i):
        print(" ", end=" ")
    for k in range(1 , i+1):
        print(k , end=" ")
    for l in range(i-1 , 0 , -1):
        print(l,end=" ")
    print()

for i in range(1 , 6):
    for j in range(6-i):
        print(" ", end=" ")
    for k in range( 1, i+1 ):
        print(k, end=" ")
    for l in range(i-1 , 0 , -1):
        print(l , end=" ")
    print()


for i in range(6 , 0 , -1):
    for j in range(6-i):
        print(" ", end=" ")
    
    for k in range(1 , i+1):
        print(k , end=" ")
    for l in range(i-1 , 0 , -1):
        print(l , end=" ")
    print()

num = 1
for i in range( 1, 6 ):
    for j in range(1 , i):
        print(num , end=" ")
        num+=1
    print()


#Pascal's Triangle Pattern


for i in range(6):
    num = 1
    for j in range(6-i):
        print(" ", end=" ")
    for k in  range(i+1):
        print(num , end="   ")
        num = num * (i-k) // (k +1)
    print()


for i in range( 6):
    num = 1
    for j in range(6 - i ):
        print(" " , end=" ")
    for k in range(i+1):
        print(num , end="  ")
        num = num * (i - k ) // (k+1)
    print()




#prime nnumber code 
def prime(num , i = 2):
    if num <= 1 :
        return False
    if num == i :
        return True
    if num % i==0:
        return False
    return prime(num , i+1)

def range_prime(start , end ):
    for i in range(start , end):        
        if prime(i):
            print(f"range of prime {i}")

range_prime(5 , 10)
# if prime(7):
#     print("Number is prime ")
# else:
#     print("number is not prime ")

#fibonachii 

# def fib(num):
#     if num<= 1:
#         return num
#     return fib(num-2)+fib(num-1)

# for i in range(10) :
#     print(f"fibo:{fib(i)}")
    
#palindrom number 
# def reve(num , rev = 0 ):
#     if num == 0 :
#         return rev
#     return reve(num // 10 , rev * 10 + (num % 10))
# n = 112211
# if n == reve(n):
#     print("number is palindrom ")
# else:
#     print("number is not palindrom ")