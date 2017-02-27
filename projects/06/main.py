import sys

from parser import Parser


def main(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    parser = Parser(input=file_contents)
    with open(destination_file) as d:
        while parser.hasMoreCommands():
            parser.advance()
            current_command_type = parser.commandType()
            if current_command_type == 'A_command':
                d.write('0' + parser.symbol())
            elif current_command_type == 'C_command':
                d.write('111' + parser.comp() + parser.dest() + parser.jump())
            elif current_command_type == 'L_command':

            



if __name__ == '__main__':
    main(sys.argv[1])
