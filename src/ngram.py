import re


class NGram:
    def __init__(self, text, pad='_', N=2):
        if not isinstance(text, str):
            raise ValueError("Text sould be string")
        if not text:
            raise ValueError("Text should not be empty")
        if not (1 <= N <= 5):
            raise ValueError("N is out of range 1 to 5")
        if not (len(pad) == 1):
            raise ValueError("Length of the pad should be 1")

        self.__text = self.__discard(text)
        self.__pad = pad
        self.__N = N

    def __tokenize(self, text):
        return text.split()

    def __discard(self, text):
        pattern = r'[,\/.?"\-!:;\*#0-9\[\]\(\)@\\\n]'
        replace = re.compile(pattern)
        text = replace.sub(' ', text)
        return self.__tokenize(text)

    def __add_pad(self, N):
        return [self.__pad * N + string + self.__pad * N for string in self.__text]

    def __generate_ngram(self, N):
        strings = self.__add_pad(N - 1)
        return [string[i:i + N] for string in strings for i in range(len(string) - (N - 1))]

    def __analyse_tokens(self):
        return [self.__generate_ngram(i) for i in range(1, self.__N + 2)]

    def __occurrence(self):
        items = self.__analyse_tokens()
        occurrence = {}
        for item in items:
            for string in item:
                if string in occurrence:
                    occurrence[string] = occurrence[string] + 1
                else:
                    occurrence[string] = 1
        return sorted(occurrence, key=occurrence.get, reverse=True)

    def rank(self):
        occurrences = self.__occurrence()
        rank = {}
        for i in occurrences:
            rank[i] = occurrences.index(i) + 1
        return sorted(rank, key=rank.get, reverse=True)
