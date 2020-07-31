#Some handy Algorithms to find Solutions of Equations of One Variable

def muller_method(f, p0, p1, p2, tol=0.00000001, N=100):
    """
    This Algorithm first presented by D.E. Muller finds the solution to f(x)=0
    given three aproximates, p0, p1, p2.
    f is defined here as a lambda function, p0-p2 are its approximate solutions.
    Tolerance is the least change to our solution we are willing to have before return a value
    n0 is the maximum number of iterations before we return failure.
    """
    #print('Muller\'s Method Called...')
    h1 = p1-p0
    h2 = p2-p1
    d1=(f(p1)-f(p0))/h1
    d2=(f(p2)-f(p1))/h2
    d=(d2-d1)/(h2+h1)
    i=3

    while i <= N:
        b=d2+h2*d
        D=((b*b) - 4 * (f(p2)*d))**(1/2)
        E=0
        if abs(b - D) < abs(b+D):
            E=b+D
        else:
            E=b-D
        h=-2 * f(p2)/E
        p=p2+h
        #print(i, p, sep=' | ')

        if(abs(h)<=tol):
            return p #Procedure was successful

        #Else: Prepare for next iteration
        p0=p1
        p1=p2
        p2=p
        h1=p1-p0
        h2=p2-p1
        d1=(f(p1)-f(p0))/h1
        d2=(f(p2)-f(p1))/h2
        d=(d2-d1)/(h2+h1)
        i+=1

    return 'failure'

def secant_method(f, p0, p1, tol=0.00000001, N=100):
    #find f(x)=0 given initial approximations p0 and p1
    #print('Secant Method Called...')
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i<=N:
        p = p1-q1*(p1-p0)/(q1-q0)
        #print(i, p, sep=' | ')
        if abs(p-p1) < tol:
            return p

        i+=1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    #if method failed to converge
    return 'failure'
"""
f = lambda x: x**4 - 3*x**3 + x**2 + x + 1
print(muller_method(f, 0.5, 1.0, 1.5))
print(secant_method(f, 0.5, 1.0))
"""
