# Two Types of String Interpolation or formatting is possible in python
# 1. Using % format formatting:

name = "Pramod V Naik"
age = 23

print("My name is %s" % name)   # My name is Pramod V Naik


print("My Name is %s and My age is %d" % (name,age))        # My Name is Pramod V Naik and My age is 23

print("------------------------------------------------")
# 2. str.format() Function

print("My Name is {} and My age is {}".format(name,age))        #My Name is Pramod V Naik and My age is 23

print("My Name is {0} and My age is {1}".format(name,age))      #My Name is Pramod V Naik and My age is 23

print("------------------------------------------------")

# 3. f-String 

print(f"My Name is {name} and My age is {age}")  #OR

print(F"My Name is {name} and My age is {age}")  

#We can easily use the string methods inside the {}
print(F"My Name is {name.upper()} and My age is {age}") 

print("------------------------------------------------")


x =10
y = 20

res = f"The add of {{x + y}} is {{{x+y}}}"

print(res)
