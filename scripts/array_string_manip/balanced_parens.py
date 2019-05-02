
def check_balanced(s):
    stack = []
    for c in s:
        if is_open(c):
            stack.append(c)
        if is_close(c):
            opening = stack.pop()
            if opening != c:
                return False
    return True

if __name__ == '__main__':

    inputs = [
        
    ]
