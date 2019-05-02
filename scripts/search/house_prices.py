def minimumLoss(p):
    pd = [(p,i) for (i,p) in enumerate(p)]
    pd.sort()
    minloss = sys.maxsize
    for i in range(n):
        for j in range(i+1, n):
            diff = pd[j][0] - pd[i][0]
            if pd[i][1] > pd[j][1]:
                minloss = min(minloss, diff)
                break
            elif diff > minloss:
                break
    return minloss