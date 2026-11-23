text = input("Введите произвольный текст: ")
old_str, new_str = input("Введите две строки через пробел (что заменить и на что): ").split()

result = text.replace(old_str, new_str)
print(result)
