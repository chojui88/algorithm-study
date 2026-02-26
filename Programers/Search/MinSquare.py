def solution(sizes):
    wide = []
    high = []
    for i in sizes:
        n = 0
        w,h = i
        if w<h:
            n = h
            h = w
            w = n
        wide.append(w)
        high.append(h)
    return max(wide) * max(high)
