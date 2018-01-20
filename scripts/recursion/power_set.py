

def power_set(s):
    '''
    the idea is that you either include each item in the set or you do not 
    and for both options you have to collect all future sets

    O(2^n)
    '''

    if len(s) == 0:
        return ['']
    else:
        suffixes = power_set(s[1:])
        sets = suffixes
        sets += [s[0] + suf for suf in suffixes]
        return sets


if __name__ == '__main__':
    inputs = [
        'asdfghj'
    ]
    for i in inputs:
        print(power_set(i))