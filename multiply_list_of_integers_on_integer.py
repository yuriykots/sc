# Write a program that takes one array representing integers and one integer,
# and return an array of integers representing their product


test_num1 = [1, 3, 4, 6]
test_num2 = 3


def multiply_two_numbers(num1, num2):
    is_result_negative = False

    if num1[0] < 0:
        is_result_negative = True

    num1[0] = abs(num1[0])

    result = []
    for i in reversed(range(len(num1))):
        result.insert(0, num1[i] * num2)

    for i in reversed(range(len(result))):
        if result[i] >= 10:
            # Inserting a number to the list
            if i == 0:
                result.insert(0, result[i] // 10)
                result[i + 1] = result[i + 1] % 10
            else:
                result[i-1] = result[i-1] + (result[i] // 10)
                result[i] = result[i] % 10

    if is_result_negative:
        result[0] = result[0] * -1

    print(result)
