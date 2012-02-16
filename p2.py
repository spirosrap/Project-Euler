def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print fib(5);

def tot():
  total=0;
  i=0;
  while (fib(i) < 4000000):
     if(fib(i)%2==0):
       total+=fib(i);
     i+=1;
  return total;

print tot();