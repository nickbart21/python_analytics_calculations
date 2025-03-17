import numpy as np

#takes in a numpy array of numbers and returns the count of even numbers
def count_evens(x):

    even_counter = 0

    for i in range(len(x)):
        for j in range(len(x)):
            if (x[i, j] % 2) == 0:
                even_counter = even_counter + 1

    return even_counter

# takes in a numpy array of numbers and returns the mean of the numbers in array positions
# where i + j are divisible by 5
def mean_of_nums_divby5(x):

    sum1 = 0
    counter = 0

    for i in range(len(x)):
        for j in range(len(x)):
            if (i + j) % 5 == 0:
                sum1 = sum1 + x[i, j]
                counter = counter + 1

    mean1 = sum1 / counter

    return mean1


if __name__ == "__main__":
    x1 = np.random.randint(low=0, high=1000, size=(10, 10))
    print(x1)

    even_count = count_evens(x1)
    print(f"\nThere are {even_count} even numbers in the array")

    initial_mean = 1
    sdev = .5
    x2 = sdev * np.random.randn(8, 9) + initial_mean
    print("\n", x2)

    result_mean = mean_of_nums_divby5(x2)
    print(f"\nThe mean of indexes that satisfy 'i+j % 5 == 0' is: {result_mean}")

