single_str =" hellow hellow hellow  teqstar"

multi_str = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua """

print(single_str)
print(multi_str)

# Get the character at position
print("position",single_str[1])

print("length of sting ",len(single_str))

#  Slicing Strings
print(single_str[1:5])

#ending
print(single_str[:5])

#starting
print(single_str[2:])

#back-word index
print(single_str[::-1])

# modification of string and methods
print(single_str.upper())#print upper case
print(single_str.lower())#print lower case
print(single_str.strip())# removed space
print("total count 1" , single_str.count("hellow"))
print(single_str.replace("teqstar" , "world")) #change  substring

# string formating

price = 30
print(f"For only {price} dollars!")


x = "Hello"
y = False

print(bool(x)) # this methos is use to chack variable are Booleans or not
print(bool(y))