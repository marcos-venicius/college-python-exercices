class Prompter:
    def __init__(self, infinit: bool = False, trim: bool = False):
        self.__infinit = infinit
        self.__trim = trim

    def prompt(self, question: str):
        data = input(question)

        if self.__trim:
            data = data.strip()

        if not self.__infinit:
            return data

        yield data

        yield from self.prompt(question)


