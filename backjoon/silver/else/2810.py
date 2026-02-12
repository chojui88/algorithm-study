#극장 한 줄이 있는 자리
n = int(input())
seats = input()

#ll 이 있다면 count+= 1
couple = seats.count("LL")

people = min(n,n + 1 - couple)
print(people)