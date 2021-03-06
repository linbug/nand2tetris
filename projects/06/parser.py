import code_module


class Parser:
    def __init__(self, input):
        self.input = input.splitlines()
        self.current_command = None

    def line_is_comment(self, line):
        line = line.strip()
        return (line.startswith('//') or line=="")

    def hasMoreCommands(self):
        """
        Are there more commands in the input?
        """
        while len(self.input) and self.line_is_comment(self.input[0]):
            self.input.pop(0)
        return bool(len(self.input))

    def advance(self):
        """
        Reads the next command from the input and makes it the current
        command. Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """
        line = self.input.pop(0)
        comment_index = line.find('//')
        if comment_index>=0:
            line = line[:comment_index]
        self.current_command = line.strip()

    def commandType(self):
        """
        Returns the type of the current
        command:
        - A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        - C_COMMAND for dest=comp;jump
        - L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol.
        """
        if self.current_command.startswith('('):
            return 'L_command'
        elif self.current_command.startswith('@'):
            return 'A_command'
        elif any (c in ['=', ';'] for c in self.current_command):
            return 'C_command'
        else:
            raise AttributeError('invalid line: {}'.format(self.current_command))

    def symbol(self):
        """
        Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).
        Should be called only when commandType() is A_COMMAND or L_COMMAND.
        """
        symbol = self.current_command[1:]
        if self.current_command.startswith('('):
            return symbol[:-1]
        else:
            return symbol

    def dest(self):
        """
        Returns the dest mnemonic in the current C-command (8 possibilities).
        Should be called only when commandType() is C_COMMAND
        i.e., return the binary for dest from
        dest=comp;jump or
        dest=comp
        otherwise for null
        """
        equals_index = self.current_command.find('=')
        if equals_index<0: # comp
            mnemonic = 'null'
        # dest=comp;jump or dest=comp
        else:
            mnemonic = self.current_command[:equals_index]
        return code_module.dest(mnemonic)

    def comp(self):
        """
        return the binary for comp from
        dest=comp;jump or
        comp;jump      or
        dest=comp
        """
        equals_index = self.current_command.find('=')
        semicolon_index = self.current_command.find(';')
        if equals_index<0: # comp;jump
            mnemonic = self.current_command[:semicolon_index]
        elif semicolon_index<0: # dest=comp
            mnemonic = self.current_command[(equals_index+1):]
        else: # dest=comp;jump
            mnemonic = self.current_command[(equals_index+1):semicolon_index]
        return code_module.comp(mnemonic)

    def jump(self):
        """
        return the binary for jump from
        dest=comp;jump or
        comp;jump
        otherwise for null
        """
        semicolon_index = self.current_command.find(';')
        if semicolon_index<0: # dest=comp or comp
            mnemonic = 'null'
        else: #...;jump
            mnemonic = self.current_command[(semicolon_index+1):]
        return code_module.jump(mnemonic)
