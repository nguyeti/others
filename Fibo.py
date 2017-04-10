# normal (list)
def fibo(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a+b (equivalent à: t=a, a=b, b=t+b)

    return output


print(fibo(10))
#>> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#avec generator
def genfibo(n):
    a = 1
    b = 1
    
    for i in range(n):
        yield a
        a, b = b, a+b

a = genfibo(10)

for i in a:
    print(i)
#
#>> 1
#1
#2
#3
#5
#8
#13
#21
#34
#55

#list = everything is kept in memory so if we do fibo(10000000000000000000000000000000000000000....) it is gonna take a lot of memory.
#Generator does not keep everything in memory. It only keeps the "current" value and call next() to get the next value until it reaches the end, which would trigger the Stop Iteration error
