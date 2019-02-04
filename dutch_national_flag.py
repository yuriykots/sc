# Write a program that takes an array A and an index i into A, and rearranges the elements such that element less than
# A[i] (the "pivot" appear first, followed by elements equal to the pivot, followed by elements greater than pivot.

test_num = [3, 5, 0, 5, 3, 0]
test_pivot_index = 0
test_result = [0, 0, 3, 3, 5, 5]


def rearrange_number_list(number_list, pivot_index):
    num1 = []
    num2 = []
    num3 = []
    pivot = number_list[pivot_index]

    for i in range(len(number_list)):
        if number_list[i] < pivot:
            num1.append(number_list[i])
        elif number_list[i] == pivot:
            num2.append(number_list[i])
        elif number_list[i] > pivot:
            num3.append(number_list[i])

    result = []

    for i in range(len(num1)):
        result.append(num1[i])

    for i in range(len(num2)):
        result.append(num2[i])

    for i in range(len(num3)):
        result.append(num3[i])

    print('Result: {}'.format(result))
    return result


if test_result == rearrange_number_list(test_num, test_pivot_index):
    print('Test passed')


# Solution 2

test_num = [3, 5, 0, 5, 3, 0]
test_pivot_index = 0
test_result = [0, 0, 3, 3, 5, 5]


def rearrange_number_list_two(number_list, pivot_index):
    pivot = number_list[pivot_index]

    # group element smaller than pivot
    for i in range(len(number_list)):
        if number_list[i] < pivot:
            break

        for j in range(i+1, len(number_list)):
            if number_list[j] < pivot:
                number_list[i], number_list[j] = number_list[j], number_list[i]
                break

    print('result after first loop: {}'.format(number_list))

    # group element larger than pivot
    for i in reversed(range(len(number_list))):
        if number_list[i] < pivot:
            break

        for j in reversed(range(i)):
            if number_list[j] > pivot:
                number_list[i], number_list[j] = number_list[j], number_list[i]
                break

    print('result {}'.format(number_list))
    return number_list


if test_result == rearrange_number_list_two(test_num, test_pivot_index):
    print('Test passed')


test_num = [4, 4, 2, 2, 0, 0]
test_pivot_index = 2
test_result = [0, 0, 2, 2, 4, 4]


def rearrange_number_list_three(number_list, pivot_index):
    pivot = number_list[pivot_index]

    swap_index = 0

    for i in range(1, len(number_list)):
        if number_list[i] < pivot:
            number_list[swap_index], number_list[i] = number_list[i], number_list[swap_index]
            swap_index += 1

    print('result after first loop {}'.format(number_list))
    swap_index = len(number_list) - 1

    for i in reversed(range(len(number_list) - 1)):
        if number_list[i] < i:
            break

        if number_list[i] > pivot:
            number_list[i], number_list[swap_index] = number_list[swap_index], number_list[i]
            swap_index -= 1

    print('result {}'.format(number_list))
    return number_list


if test_result == rearrange_number_list_three(test_num, test_pivot_index):
    print('Test passed')


