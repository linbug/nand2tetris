class Parser:
    def __init__(self, input):
        self.input = input.splitlines()

    def line_is_comment(self, line):
        line = line.strip()
        return line.startswith('//')

    def hasMoreCommands(self):
        while len(self.input) and line_is_comment(self.input[0]):
            self.input
        






