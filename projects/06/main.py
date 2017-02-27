import sys

from parser import Parser


def main(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    parser = Parser(input=file_contents)
    basename = file_name[:file_name.find(".asm")]
    dest_name = basename+".hack"
    with open(basename+".hack",'w') as d:
        while parser.hasMoreCommands():
            parser.advance()
            current_command_type = parser.commandType()
            if current_command_type == 'A_command':
                d.write('0' + parser.symbol())
            elif current_command_type == 'C_command':
                d.write('111' + parser.comp() + parser.dest() + parser.jump())
            d.write("\n")

if __name__ == '__main__':
    main(sys.argv[1])
