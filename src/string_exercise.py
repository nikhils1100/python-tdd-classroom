class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        # index postions : [start,stop,step]
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if character in vowels:
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        if len(sentence)==0:
            return ''
        if sentence == ' ':
            return ''

        sentence_list = sentence.split(' ')

        index = 0
        sentence_list_wordslen = list(map(lambda x: len(x), sentence_list))
        max_len = 0

        for i, word_len in enumerate(sentence_list_wordslen):
            if word_len > max_len:
                max_len = word_len
                index = i

        return sentence_list[index]

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        text_list = text.split(' ')
        text_list_wordslen = list(map(lambda x: len(x), text_list))
        return text_list_wordslen