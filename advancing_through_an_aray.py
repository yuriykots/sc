# Write a program which takes an array of n integers, where A[i] denotes the maximum you can advance from index i,
# and returns whether it is possible to advance to the last index starting from the beginning of the array

test_num = [3, 3, 1, 0, 2, 0, 1]
test_result = True


def can_reach_end(num_list):
    furthest_reach_so_far_index = 0

    for i in range(len(num_list) - 1):
        if i > furthest_reach_so_far_index:
            break

        furthest_reach_so_far_index = max(furthest_reach_so_far_index, num_list[i] + i)

    print('is_possible_to_advance_to_the_end: {}'.format(furthest_reach_so_far_index >= (len(num_list) - 1)))
    return furthest_reach_so_far_index >= (len(num_list) - 1)


if test_result == can_reach_end(test_num):
    print('Test passed')
