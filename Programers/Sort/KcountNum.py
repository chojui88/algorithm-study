def solution(array,commands):
    result = []
    for a in commands:
        i,j,k = a
        newArray =array[i-1:j]
        newArray.sort()
        result.append( newArray[k-1])
    return result
