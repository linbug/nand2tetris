from code_module import dest, jump, comp
from symbol_table import SymbolTable # thsi still needs to be implemented

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
        while len(self.input) and line_is_comment(self.input[0]):
            self.input.pop(0)
        return bool(len(self.input))

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
        if SymbolTable.contains(self.current_command):
            return 'L_command'
        elif self.current_command.startswith('@') and\
             (self.current_command[1:].isdigit() or\
              SymbolTable.contains(self.current_command[1:]):
            return 'A_command'
        elif any (c in ['=', ';'] for c in self.current_command):
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
        i.e., return dest from
        dest=comp;jump or
        dest=comp
        otherwise return null
        """
        equals_index = self.current_command.find('=')
        if equals_index<0: # comp
            return 'null'
        # dest=comp;jump or dest=comp
        else:
            return self.current_command[:equals_index]

    def comp(self):
        """
        return comp from
        dest=comp;jump or
        comp;jump      or
        dest=comp
        """
        equals_index = self.current_command.find('=')
        semicolon_index = self.current_command.find(';')
        if equals_index<0: # comp;jump
            return self.current_command[:semicolon_index]
        else if semicolon_index<0: # dest=comp
            return self.current_command[(equals_index+1):]
        else: # dest=comp;jump
            return self.current_command[(equals_index+1):semicolon_index]

    def jump(self):
        """
        return jump from
        dest=comp;jump or
        comp;jump
        otherwise return null
        """
        semicolon_index = self.current_command.find(';')
        if semicolon_index<0: # dest=comp or comp
            return 'null'
        else: #...;jump
            return self.current_command[(semicolon_index+1):]
