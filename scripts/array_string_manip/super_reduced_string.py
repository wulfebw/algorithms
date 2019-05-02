def super_reduced_string(s):
    i = 0
    n = len(s)
    while i < n - 1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            n = len(s)
            i = max(0, i - 1)
        else:
            i += 1
    if s == '':
        return "Empty String"
    else:
        return s