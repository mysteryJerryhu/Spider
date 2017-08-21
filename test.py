# -*- coding:UTF-8 -*-
# Output from large to small
"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

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
"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""


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
