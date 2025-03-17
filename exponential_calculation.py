
#calculates the result of an exponential of x1 to the power of n
def exponential(x, n):
    x = float(x)
    result = float(0)

    temp_result = x
    i = 0
    abs_n = (abs(n))

    for i in range(abs_n - 1):
        result = temp_result * x
        temp_result = result

        i += 1

    if n < 0:
        result = 1.00 / result
    elif n == 0:
        result = 1

    return result, x, n

if __name__ == "__main__":

    exp1, x1, n1 = exponential(x=2, n=10) #1024.0
    exp2, x2, n2 = exponential(x=3, n=-3) #0.037

    print(f"\nThe result of {x1} to the power of {n1} is: {exp1}")
    print(f"\nThe result of {x2} to the power of {n2} is: {exp2}")