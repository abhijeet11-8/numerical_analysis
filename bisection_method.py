class bisection_method:
    def __init__(self, func, a, b, hor_tol=1e-5, ver_tol=1e-5,max_iter=100):
        self.func, self.a, self.b, self.hor_tol, self.ver_tol, self.max_iter = func, a, b, hor_tol, ver_tol, max_iter

    @staticmethod
    def sign(x):
        if x < 0: return -1
        elif x > 0: return +1
        else: return 0

    def __call__(self):

        '''Bisection method to find the root of a function in the interval [a, b].
        
        Parameters:
        func : callable
            The function for which we want to find the root.
        a : float
            The start of the interval.
        b : float
            The end of the interval.

        f(a) ,f(b) must have opposite signs.
            
        her_tol : float
            The tolerance for convergence on x axis.
        ver_tol : float
            The tolerance for convergence on y axis.
        max_iter : int
            The maximum number of iterations.
        
        Returns:
        float
            The estimated root of the function.'''
        
        u, v, e = self.func(self.a), self.func(self.b), self.b - self.a
        # print(a,b,u,v)

        for k in range(self.max_iter-1):
            e, c= e/2, self.a+e
            w = self.func(c)
            # print(k,c,w,e)
            
            if abs(e) < self.hor_tol or abs(w) < self.ver_tol: 
                return (self.a+self.b)/2

            if self.sign(w) != self.sign(v): a, u = c, w
            else: b, v = c, w

if __name__ == "__main__":

    '''define a function to find the root'''
    # For example
    def f(x):
        return x**2 - 4
        
    '''Pick a, b such that f(a), f(b) has opposite signs -> f(a)*f(b) < 0'''
    root = bisection_method(f, a = 3, b= 1, hor_tol=1e-5, ver_tol=1e-5, max_iter=100)
    print("Root for f(x) is = ",root())
