import random


class Reader:
    def read(self, file_name):
        with open(file_name) as file:
            quotes = file.readlines()
        return quotes

    def get_single_quote(self, file_name):
        quotes = self.read(file_name)
        position = random.randint(0, len(quotes))
        return quotes[position]

