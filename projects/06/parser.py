from symbol_table import SymbolTable # thsi still needs to be implemented


class Parser:
    def __init__(self, input):
        self.input = input.splitlines()
        self.current_command = None

    def line_is_comment(self, line):
        line = line.strip()
        return line.startswith('//')

    def hasMoreCommands(self):
        """
        Are there more commands in the input?
        """
        while len(self.input) and line_is_comment(self.input[0]):
            self.input.pop(0)
        return len(self.input)

    def advance(self):
        """
        Reads the next command from the input and makes it the current
        command. Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """
        self.current_command = self.input.pop(0)

    def commandType(self):
        """
        Returns the type of the current
        command:
        - A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        - C_COMMAND for dest=comp;jump
        - L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol.
        """
        if SymbolTable.contains(symbol):
            return 'L_command'
        elif self.current_command.startswith('@') and self.current_command[1:].isdigit():
            return 'A_command'
        elif any (substring in ['=', ';'] for  substring in self.current_command):
            return 'C_command'
        else:
            raise AttributeError('Given symbol {} does not exist'.format(self.current_command))

    def symbol(self):
        """
        Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).
        Should be called only when commandType() is A_COMMAND or L_COMMAND.
        """
        return SymbolTable.GetAddress(self.current_command)

    def dest(self):
        """
        Returns the dest mnemonic in the current C-command (8 possibilities).
        Should be called only when commandType() is C_COMMAND
        """
        index = self.current_command.find('=')
        if index<0:
            return 'null'
        return self.current_command[:index]

    def comp(self):
        equals_index = self.current_command.find('=')
        semicolon_index = self.current_command.find(';')
        if equals_index<0:
            return self.current_command[:semicolon_index]
        return self.current_command[equals_index:]

        

                                            













