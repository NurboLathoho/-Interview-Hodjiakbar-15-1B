# 5) Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой. Результат: "AAiddialneat” 
# 6) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “Money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1
# 7)Вам дается текст:
# Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
# Найдите все слова, которые начинаются с корня advert (регистр не должен учитываться) и превратите их все в верхний регистр.

#1
# str1 = "Aidana"
# str2 = "Adilet"
# print(str1[0],str2[0],str1[1],str2[1],str1[2],str2[2],str1[3],str2[3],str1[4],str2[4],str1[5],str2[5])

#2
# def count_words(sentence):
#     cleaned_sentence = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in sentence)
#     words = cleaned_sentence.lower().split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count

# sentence = "Money, money, money, it’s always sunny, in the richmen’s world"
# word_counts = count_words(sentence)
# for word, count in word_counts.items():
#     print(f"{word}: {count}")

#3
# import re

# text = """
# Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
# """

# pattern = r'\badvert\w*\b'
# matches = re.findall(pattern, text, flags=re.IGNORECASE)

# for match in matches:
#     text = re.sub(r'\b' + re.escape(match) + r'\b', match.upper(), text, flags=re.IGNORECASE)

# print(text)
