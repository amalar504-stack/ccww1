text = input("Введите текст: ")

words = text.split()

count = 0
for w in words:
    count = count + 1

result = ""

i = count - 1

while i >= 0:
    result = result + words[i]
    result = result + " "
    i = i - 1

print("Обратный текст:")
print(result)
