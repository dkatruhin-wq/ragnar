text = input("Введите произвольный текст: ")
word = input("Введите слово для поиска: ")

count = text.count(word)
first_index = text.find(word)
cleaned_text = text.replace(word, "")

print(f"Количество встреченных слов: {count}")
print(f"Индекс первого встреченного слова: {first_index}")
print(f"Текст без слова: {cleaned_text}")
