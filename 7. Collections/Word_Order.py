from collections import OrderedDict

t = int(input())
words = OrderedDict()

for _ in range(t):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())
