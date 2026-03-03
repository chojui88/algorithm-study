def solution(n, lost, reserve):
    all = [1] * n
    for i in lost:
        all[i-1] -= 1
    for i in reserve:
        all[i-1] += 1

    for i in range(n):
        if all[i] == 0:
            if i>0 and all[i-1] == 2:
                all[i] =1
                all[i-1] = 1
            elif i<n-1 and all[i]==0 and all[i+1] == 2:
                all[i] =1
                all[i+1] = 1

    return all.count(1) + all.count(2)
