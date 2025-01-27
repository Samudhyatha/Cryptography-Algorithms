def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Example usage
if _name_ == "_main_":
    a, b = 30, 20
    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD: {gcd}")
    print(f"x: {x}, y: {y}")