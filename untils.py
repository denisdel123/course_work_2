import os
import requests
import random
from classes import basicWord
from dotenv import load_dotenv
from classes import player

load_dotenv()
url_json = os.environ.get('URL')


def load_random_word():
    words = requests.get(url_json)
    word = words.json()
    word_random = random.randint(0, len(word) - 1)

    basic_word = basicWord.Basic_Word(word[word_random]['word'], word[word_random]['subwords'])
    return basic_word


def to_start(word, count):
    print("Введите имя игрока")

    user_name = input(": ")

    return f"Привет, {user_name}!\nСоставьте {count} слов из слова \'{word}\'\
                \nСлова должны быть не короче 3 букв \
                \nЧтобы закончить игру, угадайте все слова или напишите \'stop\' \
                \nПоехали, ваше первое слово?", user_name


def check_user_answer(user_answer):
    if len(user_answer) < 3:
        return 'слишком короткое слово'
    else:
        return 'неверно'

