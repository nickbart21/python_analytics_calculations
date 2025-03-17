

#takes list and returns the sum of even numbers
def even_num_sum(L2):

    list_sum = 0

    for num in L2:
        if num % 2:
            list_sum = list_sum + num
        num += 1
    return list_sum

# takes a list and returns the initial_mean of the list
def calc_mean(L2):

    sum_for_mean = 0
    for i in L2:
        sum_for_mean = sum_for_mean + i

    mean = sum_for_mean / len(L2)

    return mean

# takes a list of numbers and returns the sum of the numbers that are greater than 500
def sum_g500(L2):

    list_sum_g500 = 0
    for i in L2:
        if i > 500:
            list_sum_g500 = list_sum_g500 + i

    return list_sum_g500

if __name__ == "__main__":

    L2 = [879, 394, 235, 580, 628, 81, 206, 238, 927, 853, 622, 603, 110, 143, 824, 324, 343, 506, 634, 325, 258, 900, 960, 286, 449, 890, 921, 170, 888, 851]

    even_sum = even_num_sum(L2)
    list_mean = calc_mean(L2)
    g500_sum = sum_g500(L2)

    print(f"\nThe sum of the even numbers is: {even_sum}")
    print(f"\nThe mean of the list is: {list_mean}")
    print(f"\nThe sum of the numbers greater than 500 is: {g500_sum}")
