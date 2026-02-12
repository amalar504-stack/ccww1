text = input("Введите текст: ")
symbols = input("Введите набор символов: ")

words = text.split()

result = ""

for word in words:
    remove = 0 
    
    for char in word:
        for s in symbols:
            if char == s:
                remove = 1
    
    if remove == 0:
        result = result + word
        result = result + " "

print("Результат:")
print(result)
