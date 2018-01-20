
MAX_WORD_LEN = 15


def first_word(s):
    i = s.find(' ')
    if i == -1:
        return s
    else:
        return s[:i]

def word_break(s, d):
    '''
    time complexity: O(2^n), but probably a lot less
    '''

    def recurse(s):
        if len(s) <= 1:
            return [s]
        else:
            strings = []
            for suffix in recurse(s[1:]):
                w = first_word(suffix)

                # space case
                if w in d:
                    strings += [s[0] + ' ' + suffix]

                # no space case
                if len(w) < MAX_WORD_LEN:
                    strings += [s[0] + suffix]

            return strings 

    strings = recurse(s)
    valid = [s for s in strings if first_word(s) in d]
    return valid

if __name__ == '__main__':

    inputs = [
        ('aaa', set(['a', 'aa', 'aaa'])),
        ('snakesandladder', set(["snake", "snakes", "and", "sand", "ladder"]))
    ]
    expect = [
        list(sorted(['a a a', 'a aa', 'aa a', 'aaa'])),
        list(sorted(["snakes and ladder", "snake sand ladder"])),
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(list(sorted(word_break(*i))))
        print()














