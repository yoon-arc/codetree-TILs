n, k, T = input().split()
wordList = []
for _ in range(int(n)):
    word = input()
    wordList.append(word)

wordList.sort()
answer = []
for i in wordList:
    if T in i:
        # print(i)
        answer.append(i)
# print(answer)
print(answer[int(k)-1])