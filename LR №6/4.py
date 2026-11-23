text = input("Введите произвольный текст: ")
start, end = map(int, input("Введите отрезок (число1 число2 через пробел): ").split())

# Вычитаем 1 из start для перевода в индексы Python; end оставляем как есть, чтобы символ включился
substring = text[start - 1 : end]
print(substring)
