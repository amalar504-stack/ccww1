text = input("Введите текст: ")

count = 0

for char in text:
    if char == '.':
        count = count + 1
    else:
        if char == '!':
            count = count + 1
        else:
            if char == '?':
                count = count + 1

print("Количество предложений:", count)
