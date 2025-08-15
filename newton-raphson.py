class newton_raphson():
    def __init__(self, func, starting_point, diff_tol, ver_tol, max_iter):
        self.func , self.x0, self.diff_tol, self.ver_tol, self.max_iter = func, starting_point, diff_tol, ver_tol, max_iter
    
    def d_dx(self, func, x, h = 1e-5):
        return (func(x+h)-func(x-h))/(2*h)
    
    def __call__(self):
        x0, func= self.x0, self.func
        for i in range(self.max_iter):
            deriv = self.d_dx(func, x0)
            if deriv == 0:
                print("f'(x) = 0")
                return None
            x1 = x0 - func(x0)/deriv
            if abs(func(x1)) < self.ver_tol or abs(x1 - x0) < self.diff_tol:
                return x1
            else: x0 = x1
            print("No root found.")
            return None

if __name__ == "__main__":
    import numpy as np
    '''
    * function should have a real root.
    * f'(x) != 0
    > error convergence en+1 = en**2 - proove!!
    '''

    def f(x):
        return np.sin(x)**2-4
    
    root_finder = newton_raphson(f, 3.0, 1e-12, 1e-12, 1000)
    root = root_finder()
    print("Root = ", root)