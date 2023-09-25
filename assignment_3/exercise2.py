def approx_newton(value):
    Y = X/2

    while abs(Y * Y - X) > 0.001:
        Y = (Y + X/Y) / 2
    
    return Y


X = float(input("Enter a number: "))

if X > 0:
    Y = approx_newton(X)
    print(f"Square root: {Y:.3f}")
