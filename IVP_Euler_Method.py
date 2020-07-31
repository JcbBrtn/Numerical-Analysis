def euler_method(f, a, b, alpha, N=10):
    """
    -Euler's method for solving initial value problems.
    
    -f is the lambda expression of the function where y'=f(t,y)
    -a and b are endpoints
    -N is N-1 of the amount of steps going to be taken for the approximation.
    -alpha is the inital condition where f(a) = alpha
    """
    h = (b-a)/N
    t=a
    w = alpha
    print('t | w')
    print(t,w, sep=' | ')

    for i in range(1,N+1):
        w = w + h * f(t,w)
        t = a + i * h
        print(t,w,sep=' | ')

    return (t,w)

#f=lambda t,y: y - t**2 + 1
#euler_method(f, 0, 2, 0.5)

