def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word_lower = root_word.lower()
    # Создаем пустой список для хранения однокоренных слов
    same_words = []

    # Перебираем все слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Условие для добавления слова в список
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем итоговый список
    return same_words


# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)  # Вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Вывод: ['Able', 'Disable']