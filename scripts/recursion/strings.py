

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[1:-1]) + s[0]

def letters_only(s):
    if len(s) == 0:
        return ''
    else:
        rest = letters_only(s[1:])
        if 'a' <= s[0] <= 'z':
            return s[0] + rest
        else:
            return rest

def tobinary(n):
    b = ''
    if n > 1:
       b += tobinary(n//2)
    b = b + str(n % 2)
    return b

def contains(s1, s2):

    def recurse(i,j):
        if j == len(s2):
            return True
        elif i == len(s1):
            return False
        elif s1[i] == s2[j]:
            return recurse(i+1,j+1)
        else:
            return recurse(i+1,j)

    return recurse(0,0)



if __name__ == '__main__':

    for s in ['asdf', 'asdfg', 'ab', '123456789']:
        print(s)
        print(reverse(s))

    print()

    for s in ['asdf', '!!!', 'aa!', '!aa', '!aa!']:
        print(s)
        print(letters_only(s))
        print()

    print()
    for n in [0,1,2,10,11,333,4567]:
        print('{0:b}'.format(n))
        print(tobinary(n))
        print()

    print()
    for s1,s2 in [('bcd','cd'), ('asdfasdfasdf', 'asdf'), ('1110111', '101'), ('11111', '90000')]:
        print(s2 in s1)
        print(contains(s1,s2))
