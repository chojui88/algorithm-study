def solution(arr):
    result = []
    for i in arr:
        if not result or i != result[-1]:
            result.append(i)

    return result