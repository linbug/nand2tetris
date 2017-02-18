    dest_dict = {
        'null': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111',
    }

    jump_dict = {
        'null': '000',
        'JQT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111',
    }

def dest(command):
    return dest_dict[command]

def jump(command):
    return jump_dict[command]

def comp(command):
    return comp_dict[command]
