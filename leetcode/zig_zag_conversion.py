test_string = 'PAYPALISHIRING'
test_rows = 3
test_result = 'PAHNAPLSIIGYIR'

def zig_zag_conversion(s: 'str', numb_rows: 'int') -> 'str':
    rows = {}

    for i in range(numb_rows):
        rows['row{}'.format(i)] = ''

    row = -1

    go_down = False

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
