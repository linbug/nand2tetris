import sys
from parser import Parser


def format_number(symbol):
    return bin(int(symbol))[2:].zfill(15)

predefined_symbols = {
        'R0': 0,
        'R1': 1,
        'R2': 2,
        'R3': 3,
        'R4': 4,
        'R5': 5,
        'R6': 6,
        'R7': 7,
        'R8': 8,
        'R9': 9,
        'R10': 10,
        'R11': 11,
        'R12': 12,
        'R13': 13,
        'R14': 14,
        'R15': 15,
        'SP': 0,
        'LCL': 1,
        'ARG': 2,
        'THIS': 3,
        'THAT': 4,
        'SCREEN': 16384,
        'KBD': 24576,
    }

#  : (LABEL)              --->               
# 0: M=D                  ---> 00010101000100
# 1: D+A                  ---> 01001010010010
# 2: ??                   ---> 00100101010111
# 3: @i = 4               ---> 01001111001111
# 4: D=A+i                ---> 00001010010111
# 5: JMP@ANOTHER_LABEL    ---> 10110101011110
#  : (ANOTHER_LABEL)      --->               
# 6: JMP;@variable        ---> 00010100110101

# 0: 32
# 1: 11
# 2: 949
# 3: 0
# 4: 0

def main(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    parser = Parser(input=file_contents)
    basename = file_name[:file_name.find(".asm")]
    dest_name = basename+".hack"
    symbol_table = predefined_symbols.copy()
    line = 0
    next_var = 16
    while parser.hasMoreCommands():
        parser.advance()
        current_command_type = parser.commandType()
        if current_command_type == 'L_command':
            symbol_table[parser.symbol()] = line
        else:
            line += 1
            if current_command_type == 'A_command':
                symbol = parser.symbol()
                if not symbol.isdigit() and symbol not in symbol_table:
                    symbol_table[symbol] = next_var
                    next_var += 1
    parser = Parser(input=file_contents)
    with open(basename+".hack",'w') as d:
        while parser.hasMoreCommands():
            parser.advance()
            current_command_type = parser.commandType()
            if current_command_type == 'A_command':
                symbol = parser.symbol()
                if not symbol.isdigit():
                    symbol = symbol_table[symbol]
                d.write('0' + format_number(symbol) + '\n')
            elif current_command_type == 'C_command':
                d.write('111' + parser.comp() + parser.dest() + parser.jump() + '\n')

if __name__ == '__main__':
    main(sys.argv[1])
