n, k, T = input().split()
wordList = []
for _ in range(int(n)):
    word = input()
    wordList.append(word)

wordList.sort()
answer = []
for i in wordList:
    if i[:len(T)] == T:
        answer.append(i)
print(answer[int(k)-1])