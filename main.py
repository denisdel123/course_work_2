from classes import player
from untils import to_start, load_random_word, check_user_answer

if __name__ == '__main__':
    basic = load_random_word()
    info, user_name = to_start(basic.word, basic.word)
    print(info)
    player = player.Player(user_name)

    while basic.word_math() != player.word_math():
        user_answer = input(':')
        if user_answer == 'stop' or user_answer == 'стоп':
            break
        else:
            if basic.check_words(user_answer):
                if user_answer in player.use_set_words:
                    print("уже использовано")
                else:
                    player.add_word_in_use(user_answer)
                    print("верно")
            else:
                print(check_user_answer(user_answer))

    print(f"Игра завершена, вы угадали {player.word_math()} слов")

