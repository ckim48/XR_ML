import pandas

print("Hello")
x = 15 # integer type
print(x) # Comments
# 4 types of variables
y = 2.14 #float type --> decimal
z = "Hello" # String type --> Text
a = True  # Boolean type ---> True/False
# Variable Name
# There should no space on variable name
# No special characters

x = 2
y = 3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % y) # Modulo

x = 2
if x > 5:
    print("Big")
elif x > 1:
    print("Mid")
else:
    print("Small")

# list --> is for storing multiple values
lst = [10,2,4,22]
print(lst)
print(len(lst)) # len prints the number of items in list
# index --> indicates the position of the item in list
# index starts from 0
print(lst[1]) # 2

# lst = [10, 2, 4, 22]
for i in lst:
    print(i)

# dictionary --> is for storing multiple values
# each item in dictionary has key and value
# dictionary -> {}, list -> [ ]
d = {"scott": 3}
print(d["scott"]) # 3

# library --> pandas --> open source library that helps
#                        us to do data analysis using python
data = {"name": ["Scott", "Alice", "Jason"], "GPA": [3.0, 4.0, 3.7] }
print(data) # {'name': ['Scott', 'Alice', 'Jason'], 'GPA': [3.0, 4.0, 3.7]}
# Dataframe --> new type that shows the data in tabular format
df = pandas.DataFrame(data)
print(df)
print(df["name"])

# Main APP --> VR

# Machine Learning

# Main purpose of our project

# We are going to create web-based dashboard
# to show some the result of data analysis

# We are going to who people feel when the consulting with AI consultant

