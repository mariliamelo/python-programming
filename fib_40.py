fib = [0,1]
i = 0
print fib

while i < 40:
    print fib[-1], fib[-2]
    new = fib[-1] + fib[-2]
    fib.append(new)
    i += 1
    
print fib
print "The 40th fibbonacci number is",fib[-1]
