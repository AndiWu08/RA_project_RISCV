import functions

opcode, operands = functions.clean_line(['jalr', 'x0, ', '0(x5)'])

functions.read_file('./test/jumps.txt')