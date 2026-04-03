
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)



def exp_x(x, n):
    abs_val = lambda t: t if t >= 0 else -t
    
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        result += abs_val(term)
    
    return result



result = 0  

def geometric_series(n, r, i=0):
    global result
    
    if i > n:
        return
    
    result += r ** i
    geometric_series(n, r, i + 1)




x = float(input("Enter x: "))
n = int(input("Enter n (for exp_x): "))
print("exp_x result:", exp_x(x, n))


n2 = int(input("Enter n (for geometric series): "))
r = float(input("Enter r: "))

geometric_series(n2, r)
print("Geometric series result:", result)
