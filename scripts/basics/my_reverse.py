

def my_reverse(string):
    med = len(string) / 2
    size = len(string) - 1
    for i in range(med):
        string[i], string[size - i] = string[size - i], string[i]
    return ''.join(string)

def my_reverse_2(string):
    med = len(string) / 2
    size = len(string) - 1
    for i in range(med):
        temp = string[i]
        string[i] = string[size - i]
        string[size - i] = temp
    return ''.join(string)


if __name__ == '__main__':
    string = list('fasdfasdfsdkljhasldfkjahs')
    actual = my_reverse_2(string)
    expected = ''.join(string)
    assert actual == expected

    string = list('k')
    actual = my_reverse_2(string)
    expected = ''.join(string)
    assert actual == expected

    string = list('')
    actual = my_reverse_2(string)
    expected = ''.join(list(string))
    assert actual == expected
