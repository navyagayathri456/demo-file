def fib(n):
   f=[]
   f[0],f[1] = 0,1
   if n==0:
       return f[0]
    if n==1:
        return f[1]
    for i in range(2,len(n)):
        f[i]=f[i-1] + f[i-2]
    return f

printf(fib(100))

...
   O(2^n)
... 