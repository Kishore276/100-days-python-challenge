import cmath
def find_quadratic_roots(a, b, c):
    """Finds the roots of the quadratic equation ax^2 + bx + c = 0."""
    D = b**2 - 4*a*c  # Discriminant
    root1 = (-b + cmath.sqrt(D)) / (2 * a)
    root2 = (-b - cmath.sqrt(D)) / (2 * a)
    return root1, root2
a = 2
b = 3
c = -2
roots = find_quadratic_roots(a, b, c)
print(f"The roots of the equation {a}x^2 + {b}x + {c} = 0 are: {roots[0]} and {roots[1]}")