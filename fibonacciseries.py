a = int(input('enter the first element'))
b = int(input('enter the second element'))
n = int(input('enter the number of elements '))
print(a,b)
 
while n-2:
       c = a + b
       a = b
       b = c
       print(c)
       n = n-1