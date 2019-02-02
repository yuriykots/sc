# Write a program that takes two arrays representing integers,
# and return an integer representing their product


# Planning
# multiplication from school
# think out about the loop

# 123
#  21

# 3x1, 2x1, 1x1
# 3x2, 2x2, 1x2
# sum

# num1, num2
# for i reverse(num2):
#     for j in reverse(num1)

#           num1[j] x num2[i]

#           num1[2] x num2[2]
#           num1[1] x num2[2]
#           num1[0] x num2[2]

#           3 x 1
#           2 x 1
#           1 x 1


# What should be the result list?
# 99
# 99
# 9801

# 11
# 11
# 121

# result len = 4
# result len = len(num1) + len (num2)
# result = [0] * [len(num1) + len(num2)]

test_number_one = [1, 2, 3]
test_number_two = [3, 2, 1]
result_test = [-3, 9, 4, 8, 3]


def multiply_two_numbers(num1, num2):
    is_result_negative = False

    if num1[0] < 0 and num2[0] > 0:
        is_result_negative = True

    if num1[0] > 0 and num2[0] < 0:
        is_result_negative = True

    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            result[i + j + 1] += int(num1[j] * num2[i])
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] = result[i + j + 1] % 10

    if result[0] == 0:
        result = result[1:]

    if is_result_negative:
        result[0] = result[0] * -1

    print('result')
    print(result)


if result_test == multiply_two_numbers(test_number_one, test_number_two):
    print('Test passed')
