
def find_subsets(s):

    if len(s) == 0:
        return ['']
    else:
        others = find_subsets(s[1:])
        return [s[0] + o for o in others] + others

if __name__ == '__main__':
    print(find_subsets('123'))