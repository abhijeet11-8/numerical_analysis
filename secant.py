class secant:
    def __init__(self, func, x0, x1, hor_tol, ver_tol, max_iter):
        self.func, self.x0, self.x1, self.hor_tol, self.ver_tol, self.max_iter = func, x0, x1, hor_tol, ver_tol, max_iter
    def __call__(self):
        x1, x0 = self.x1, self.x0
        for i in range(self.max_iter):
            fx1, fx0 = self.func(x1), self.func(x0)
            x2 = x1 - fx1*(x1 - x0)/(fx1 - fx0)
            fx2 = self.func(x2)
            if abs(fx2) < self.ver_tol or abs(x2 - x1) < self.hor_tol:
                return x2
            else: x0, x1 = x1, x2

if __name__ == "__main__":
    def f(x):
        return x**2 - 4
    

    root_finder = secant(f, 3, 2, 1e-5, 1e-5, 100)
    root = root_finder()
    print("root= ", root)
