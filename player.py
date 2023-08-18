class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.use_set_words = []

    def get_len_words(self, words):
        return len(words)

    def add_word_in_use(self, use_word):
        self.use_set_words.append(use_word)

    def check_use_word(self, word):
        if word in self.use_set_words:
            return True
        return False

    def word_math(self):
        return len(self.use_set_words)

    def __repr__(self):
        print("класс игрок")
