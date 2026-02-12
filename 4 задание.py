text = input("Введите строку: ")
char1 = input("Введите первый символ: ")
char2 = input("Введите второй символ: ")

start = -1
end_pos = -1
index = 0

for char in text:
    if char == char1:
        if start == -1:
            start = index
    if char == char2:
        if end_pos == -1:
            end_pos = index
    index = index + 1

result = ""
index = 0

for char in text:
    if start != -1:
        if end_pos != -1:
            if start < end_pos:
                if index < start:
                    result = result + char
                else:
                    if index > end_pos:
                        result = result + char
    index = index + 1

print("Результат:", result)
