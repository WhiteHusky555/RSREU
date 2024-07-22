def anan(text):
    слова = текст.split()
    for слово1 in слова:
        for слово2 in слова:
            if слово1 != слово2 and sorted(слово1.lower()) == sorted(слово2.lower()):
                return слово1, слово2

x = str(input())
result = anan(x)
print(result[0], result[1])
