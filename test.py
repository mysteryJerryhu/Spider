# -*- coding:UTF-8 -*-
# Output from large to small
x = input("x=")
y = input("y=")
z = input("z=")
m = max(x, y, z)
n = min(x, y, z)
if x != m and x != n:
    print(n, x, m)
if y != m and y != n:
    print(n, y, m)
if z != m and z != n:
    print(n, z, m)


# Fibonacci sequence:


def fib(f):                    # define a function
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else:
        return fib(int(f)-1) + fib(int(f)-2)        # 'f' is str, need force change to int
l = input("Enter number(s) of Fibonacci value:")
print("Fibonacci sequence:[", end=" ")
for i in range(0, int(l)):
    print(fib(i), end=" ")
    i += 1
print("]")
