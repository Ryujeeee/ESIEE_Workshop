# Simple Math

x = 2
y = 3
z = x + y

print(x)
print(y)

# Python is using indents

a = 10
b = 5 
c = a / b
d = a * b
e = a % b

a == b
a || b
a === b
a != b
a ^^ b
a && b

name = "Anna"
surname = "Grey"

student_name = name + " " + surname
print(student_name)

# TASK
# 1. Write IF ELSE statement to validate if x is larger than y. Return TRUE if YES

y = 5
x = 10 
if x > y:
        print(True)  

# With Function

def eval (x, y):
  if y > x:
    return True
    return False
print(eval(300,200))

# 2. Write IF ELSE statement to validate if x is larger than y and less than b. Return TRUE if YES

def compareFunc2 (x, y, b):
  if (y > x) and (x < b):
    return True
    return False

print(compareFunc2(300,200,600))



