# first

print("hello  world ")

# variable and data type

name = "harsh"
age = 21
float_var = 10.5
bool_var = True

l1 = [1,2,3]
t1 = (1,2,3)
s1 = {1,1,2,3}
disc1 = {   "name" : "harsh",
            "age" : 21
}

com1 = 1j

print("name :" , name)
print(type(name))
print("age :",age )
print(type(age))
print("float variable :" , float_var)
print(type(float_var))
print("bool var " , bool_var)
print(type(bool_var))

print("list " , l1)
print(type(l1))

print("tuple " ,t1)
print(type(t1))

print("set  " ,s1)
print(type(s1))

print("dictinary " , disc1)
print(type(disc1))

print("complex " , com1)
print(type(com1))

#assign Multiple Values
red , blue , green  = "red" , "blue" ,"green"
print(red , green , blue)

# Global Variables

a = "global variable "

def scop_var():
    a = "local variable"
    print("scop of variable  " + a)

scop_var()
print(a)


