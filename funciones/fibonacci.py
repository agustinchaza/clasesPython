def fibonacci(mes):
    if mes==1:
        return 1
    if mes==2:
        return 1

    fibo_1=fibonacci(mes-1)
    fibo_2=fibonacci(mes-2)

    return fibo_1+fibo_2
    


print (fibonacci(4))

