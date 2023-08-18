class Basic_Word:
    def __init__(self, word, set_word):
        self.word = word
        self.set_word = set_word

    def check_words(self, user_answer):
        if user_answer in self.set_word:
            return True
        return False

    def word_math(self):
        return len(self.set_word)

    def __repr__(self):
        print("класс слова")
