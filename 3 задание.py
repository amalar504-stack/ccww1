reserved_words = ["if", "else", "for", "while", "return"]

text = input("Введите текст: ")

words = text.split()

result = ""

for word in words:
    changed = word
    for rw in reserved_words:
        if word.lower() == rw:
            changed = word.upper()
    result = result + changed
    result = result + " "

print("Измененный текст:")
print(result)
