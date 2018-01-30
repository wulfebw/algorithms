

def print_all_binary(n):
    if n <= 0:
        return ['']
    else:
        substrings = print_all_binary(n-1)
        return ['0'+ s for s in substrings] + ['1'+ s for s in substrings]

if __name__ == '__main__':
    strs = print_all_binary(3)
    print(strs)

    
