import random
import time


eng_words = ['Hi','Bye','Task', 'Programm']
ru_words = ['Привет','Пока','Задача', 'Программа']
score = 0

mod = input("Выбери режим работы тренажера: 0 - добавить новые слова, 1 - тренироваться: \n")
while ((mod != '0') and (mod != '1')):
    mod = input("Недопустимый символ! Выбери 0 или 1. (0 - добавить новые слова, 1 - тренироваться) \n")

if mod == "1":
    print("Переведи как можно больше слов правильно! У тебя 10 попыток!")
    for i in range(10):
        number = random.randint(0, len(eng_words))
        print("Как переводится слово: " + eng_words[number])
        if input() == ru_words[number]:
            print("Отлично!!!")
            score += 1
        else:
            print("Нет... Это слово - " + ru_words[number])
else:
    word = input("Введите слово на русском языке: ")
    translate = input("Введите перевод этого слова: ")
    if len(word) > 0 and len(translate) > 0:
        ru_words.append(word)
        eng_words.append(translate)
        print("Слово успешно добавлено!")

def is_api_group(chat_id):
    return chat_id == GROUP_CHAT_ID


@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return
