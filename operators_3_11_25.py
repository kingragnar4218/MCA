#arithmetic operators
print("---- arithmetic operators----")
a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

#  assignment operators
print("---- assignment operators---- ")
a += 5
print(a)

a -= 5
print(a)

a *= 5
print(a)

a /= 5
print(a)

a %= 10
print(a)

a=5
a &= 3
print(a) #here in this case first we need to ceate variable after this opration will parform

a |= 3
print(a)


# Comparison Operators
# those operators are return in true or false
print("---- Comparison Operators ---- ")
print(a == b)
print(a < b)
print(a > b)
print(a != b)
print(a <= b)
print(a >= b)

# Logical Operators
# and 	Returns True if both statements are true
# or	Returns True if one of the statements is true
# not	Reverse the c, returns False if the c is true
print("---- Logical Operators ---- ")
print( a < b  and  b > a )

print( a > b  or  b < a )

print( not(a < b  and  b > a) )

#Identity Operators
# The is operator returns True if both variables point to the same object

print("---- Identity Operators----")
x = 10
y = 20
z = x

print(x is z)
print(x is y)
print(x == y)

#Membership operators
# Membership operators are used to test if a sequence is presented in an object
print("---- Membership operators----")
l1 = [1,2,3,4]
print( 2 in l1)
print( 3 not in l1)

# Bitwise Operators 
print("---- Bitwise Operators----")

a = 5
b = 3

c = a & b
print(c)

c = a | b
print(c)

c = a ^ b
print(c)

c = ~a
print(c)

c = a << 1
print(c)

c = a >> 1
print(c)


