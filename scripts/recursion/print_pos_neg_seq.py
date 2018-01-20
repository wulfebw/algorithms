import sys

def print_seq(n):
    def recurse(i, up):
        sys.stdout.write(str(i) + ' ')
        if i == n and up:
            return
        else:
            if i <= 0:
                up = True
            if up:
                i += 5
            else:
                i -= 5

            return recurse(i, up)
    recurse(n, False)

if __name__ == '__main__':
    inputs = [
        16,
        10
    ]
    for i in inputs:
        print_seq(i)
        print()