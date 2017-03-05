class SymbolTable:
    """
    Possibilities:
    Virtual registers refer to RAM addresses 0 to 15: R0 - R15
    Predefined pointers refer to RAM addresses 0 to 4: SP, LCL, ARG, THIS, THAT
    I/O pointers refer to RAM addresses 16384 and 24576: SCREEN, KBD
    Variable symbols start at RAM address 16: [User defined]
    """
    def __init__(self):
        return None

