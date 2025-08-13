def f(x):
    """Example function for which we want to find the root."""
    return x**2 - 4

def sign(x):
    if x < 0: return -1
    elif x > 0: return +1
    else: return 0

def bisection_method(func, a, b, hor_tol=1e-5, ver_tol=1e-5,max_iter=100):

    '''Bisection method to find the root of a function in the interval [a, b].
    
    Parameters:
    func : callable
        The function for which we want to find the root.
    a : float
        The start of the interval.
    b : float
        The end of the interval.
    tol : float
        The tolerance for convergence.
    max_iter : int
        The maximum number of iterations.
    
    Returns:
    float
        The estimated root of the function.'''
    
    u, v, e = f(a), f(b), b-a
    print(a,b,u,v)

    for k in range(max_iter-1):
        e, c, w = e/2, a+e, f(c)
        print(k,c,w,e)
        
        if abs(e) < hor_tol or abs(w) < ver_tol: exit

        if sign(w) != sign(v): a, u = c, w
        else: b, v = c, w