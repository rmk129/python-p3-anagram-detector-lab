# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.list_word = list(word)

    def match(self, givenlist):
        new_list = []
        for word in givenlist:
            word_brokendown = list(word)
            if sorted(self.list_word) == sorted(word_brokendown):
                new_list.append(word)
        return new_list
                

        