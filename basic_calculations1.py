
import numpy as np

#takes a list of values and returns the uniques values and total number of unique values
def unique(list1):
    unique_list = []
    x = 0
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    num_uniques = len(unique_list)

    return unique_list, num_uniques


def frequency(list1):
    frequencies1 = {}

    for item in list1:
        if item in frequencies1:
            frequencies1[item] += 1
        else:
            frequencies1[item] = 1

    most_freq_key = 0
    most_freq_val = 0

    for key, value in frequencies1.items():
        if value > most_freq_val:
            most_freq_key = key

    return frequencies1, most_freq_key

if __name__ == "__main__":

    L1 = []
    np.random.seed(56)

    # generates 10 random integers, for each integer generated, add a random number of occurrences of
    # that integer to the L1 list, then shuffle the list
    for i in np.random.randint(0, 100, 10):
        L1.extend([i] * np.random.randint(0, 100, 1)[0])

    np.random.shuffle(L1)

    list_unique, num_uniques = unique(L1)
    frequencies, most_freq = frequency(L1)

    print(f"\nThe unique values are: {list_unique}")
    print(f"\nThe number of unique values is: {num_uniques}")

    print("\nFrequency of the unique values are:\n Val : Freq")
    for key, value in frequencies.items():
        print("% d : % d" % (key, value))

    print(f"\nThe value that appears most frequent is: {most_freq}")