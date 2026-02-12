text = input("Введите строку: ")

cleaned = ""


for char in text:
    if char.isalnum():
        cleaned = cleaned + char.lower()


length = 0
for char in cleaned:
    length = length + 1

left = 0
right = length - 1

error = 0

while left < right:
    if cleaned[left] != cleaned[right]:
        error = 1
    left = left + 1
    right = right - 1

if error == 0:
    print("Это палиндром")
else:
    print("Это не палиндром")
