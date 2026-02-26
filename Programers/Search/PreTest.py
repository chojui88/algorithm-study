def solution(answers):
    one = []
    two = []
    three = []
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    count = [0,0,0]
    for i in range(len(answers)):
        one.append(i%5 + 1)
    for i in range(len(answers)):
        two.append(pattern2[i%8])
    for i in range(len(answers)):
        three.append(pattern3[i % 10])

    for i in range(len(answers)):
        if answers[i] == one[i]:
            count[0] +=1
    for i in range(len(answers)):
        if answers[i] == two[i]:
            count[1] +=1
    for i in range(len(answers)):
        if answers[i] == three[i]:
            count[2] +=1
    max_count = max(count)

    winner = []
    for i in range(3):
        if max_count == count[i]:
            winner.append(i+1)

    return winner
        