lst = [0,1]
fiban = []

def fibonacci(x, y):
    z = x + y
    lst[0] = y
    lst[1] = z
    fiban.append(x)
    return lst[0], lst[1]

user = input("Enter the Fibonacci Number: ")
for num in range(int(user)):
    fibonacci(lst[0], lst[1])

print(fiban)
