class bisection_method:
    def __init__(self, func, a, b, hor_tol=1e-5, ver_tol=1e-5,max_iter=100):
        self.func, self.a, self.b, self.hor_tol, self.ver_tol, self.max_iter = func, a, b, hor_tol, ver_tol, max_iter

    @staticmethod
    def sign(x):
        if x < 0: return -1
        elif x > 0: return +1
        else: return 0

    def __call__(self):
        u, v, e = self.func(self.a), self.func(self.b), self.b - self.a

        for k in range(self.max_iter-1):
            if self.sign(u * v)>0:
                print("Choose a and b such that f(a)*f(b) < 0")
                return
            e, c= e/2, self.a+e
            w = self.func(c)
            
            if abs(e) < self.hor_tol or abs(w) < self.ver_tol: 
                return c

            if self.sign(w) != self.sign(v): a, u = c, w
            else: b, v = c, w
        print("No root found.")
        return None

if __name__ == "__main__":
    import numpy as np
    '''
    * function should have a real root.
    * f(a) * f(b) < 0
    > error convergence en+1 = en ** 1
    '''
    def f(x):
        return np.sin(x)**2-4

    root = bisection_method(f, a = 0.0, b = 3.0, hor_tol = 1e-5, ver_tol = 1e-5, max_iter = 100)
    print("Root = ",root())
