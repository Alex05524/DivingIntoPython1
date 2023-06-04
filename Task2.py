def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}\t", end="")
        print()

# Example usage: display multiplication table up to 10
multiplication_table(10)