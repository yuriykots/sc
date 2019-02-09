# Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the
# remaining elements have been shifted left to fill the emptied indices. Return the number of valid elements.


test_num = [2, 3, 5, 5, 7, 11, 11, 11, 13]
test_result = 6


def remove_duplicates(num_list):
    filtered_list = num_list[:1]

    for i in range(1, len(num_list)):
        if num_list[i] != num_list[i-1]:
            filtered_list.append(num_list[i])

    print(filtered_list)
    return len(filtered_list)


if test_result == remove_duplicates(test_num):
    print('Test passed')
