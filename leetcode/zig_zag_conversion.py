from itertools import chain

test_string = 'PAYPALISHIRING'
test_rows = 3
test_result = 'PAHNAPLSIIGYIR'

def zig_zag_conversion(s: 'str', numb_rows: 'int') -> 'str':
    """
    :type s: str
    :type numb_rows: int
    :rtype: str
    """
    if numb_rows == 1:
        return s

    rows = [[] for i in range(numb_rows)]
    current_row = 0
    direction = +1

    for letter in s:
        rows[current_row].append(letter)
        current_row += direction

        if current_row in (0, numb_rows - 1):
            direction *= -1

    print(rows)
    return "".join(chain.from_iterable(rows))


def zig_zag_conversion_solution_two(s: 'str', numb_rows: 'int') -> 'str':
    if numb_rows == 1:
        return s

    if len(s) == 1:
        return s

    rows = {}
    row = -1

    for i in range(numb_rows):
        rows['row{}'.format(i)] = ''

    go_down = False

    if numb_rows == 2:
        for index, letter in enumerate(s):
            if index == 0:
                go_down = True

            if index % 2 == 0:
                go_down = False

            if index % 2 == 1:
                go_down = True

            if go_down:
                row = row + 1
                rows[u'row{}'.format(row)] = rows[u'row{}'.format(row)] + letter
            else:
                row = row - 1
                rows[u'row{}'.format(row)] = rows[u'row{}'.format(row)] + letter

    if numb_rows > 2:
        for index, letter in enumerate(s):
            distance = numb_rows + (numb_rows - 2)

            if index == 0:
                go_down = True

            if index == numb_rows:
                go_down = False # go up

            if index > distance:
                if index % distance == numb_rows:
                    go_down = False # go up

                if index % distance == 1:
                    go_down = True

            if go_down:
                row = row + 1
                rows[u'row{}'.format(row)] = rows[u'row{}'.format(row)] + letter
            else:
                row = row - 1
                rows[u'row{}'.format(row)] = rows[u'row{}'.format(row)] + letter

    result = ''

    for key, item in rows.items():
        result = result + item

    return result


if test_result == zig_zag_conversion(test_string, test_rows):
    print('Test passed')
else:
    print('Test failed')
