import numpy as np

# takes multidimensional array and calculates the primary and secondary diagonal sums
def diagonal_sum(x):
    prim_dsum = 0
    sec_dsum = 0

    print(x)

    for i in range(len(x)):
        prim_dsum += x[i, i]
        sec_dsum += x[i, len(x) - i - 1]

    return prim_dsum, sec_dsum

if __name__ == "__main__":
    x = np.random.randn(6, 6)

    prim_diag_sum, sec_diag_sum = diagonal_sum(x)

    print(f"\nPrimary Diagonal Sum: {prim_diag_sum}")
    print(f"\nSecondary Diagonal Sum: {sec_diag_sum}")

