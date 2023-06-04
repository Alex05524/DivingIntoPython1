def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Triangle cannot be formed with the given side lengths.")
    elif a == b and b == c:
        print("Equilateral triangle.")
    elif a == b or b == c or a == c:
        print("Isosceles triangle.")
    else:
        print("Scalene triangle.")

# Example usage:
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

classify_triangle(a, b, c)