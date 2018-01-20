

def can_parse_int(f):
    try:
        int(f)
    except:
        return False
    return True

def find_matching_parens(string, start):
    onstack = 1
    for i, char in enumerate(string[start+1:]):
        if char == ']':
            onstack -= 1
        elif char == '[':
            onstack += 1

        if onstack == 0:
            return i + start + 1
    raise ValueError('invalid string: {}'.format(string))

def decode(s):
    if s.find('[') == -1:
        return s
    else:
        f = s[0] # can't actually assume only single digit here but oh well
        if can_parse_int(f):
            c = find_matching_parens(s, 1)
            return int(f) * decode(s[2:c]) + decode(s[c+1:])
        else: # must be a letter
            return f + decode(s[1:])


if __name__ == '__main__':
    inputs = [
        '1[b]',
        '3[b2[ca]]',
        '3[a3[b]1[ab]]'
    ]
    expect = [
        'b',
        'bcacabcacabcaca',
        'abbbababbbababbbab'
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(decode(i))
        print(e == decode(i))
        print()











