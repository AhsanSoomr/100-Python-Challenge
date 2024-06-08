print("Question 1 : Swap Two Variables")

# assign a variable 
x = 5
y = 10

# here is we create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping:',x)
print('The value of y after swapping:',y)


print("-----------------------------------------")
print("----- Same Question With Fuction --------")
def swaping(x,y):
    temp = x
    x = y
    y = temp
    return x,y

x =10 
y = 20
x,y = swaping(x,y)

print('The value of x after swapping:',x)
print('The value of y after swapping:',y)







