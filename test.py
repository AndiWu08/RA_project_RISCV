import functions
import regs_and_ram

# initialize registers, ram, debug
regs = regs_and_ram.RegisterRISC()
ram = regs_and_ram.RAM()
debug = False

while True:
    print("--- simple RISCV emulator ---\n"
          "1: read .txt file with Assembler Code\n"
          "2: input Assembler Code oneliner\n"
          "3: Memory Dump\n"
          "4: print registers\n"
          "5: reset registers\n"
          "6: reset RAM\n"
          "X: EXIT\n")
    
    mode = input("select an option: ").strip().upper()

    if mode == '1':
        filepath = "./test/" + input("name of .txt file in /test: ") + ".txt"
        debug = input("enable debug-mode? y/n: ").strip().upper() == 'Y'

        instructions = functions.read_file(filepath)
        functions.run_asm(instructions, regs, ram, debug)
        
    elif mode == '2':
        asm_code = input("Assembler oneliner: ").upper().split()
        opcode, operands = functions.clean_line(asm_code)

        print(opcode, operands)
        functions.execute_opcode(opcode, operands, regs, ram)

    elif mode == '3':
        start_addr = input("start address: ")
        end_addr = input("end address: ")

        ram.memory_dump(int(start_addr), int(end_addr))

    elif mode == '4':
        print(regs)

    elif mode == '5':
        regs = regs_and_ram.RegisterRISC()
        print("Registers reseted")

    elif mode == '6':
        ram = regs_and_ram.RAM()
        print("RAM resetted")

    elif mode == 'X':
      break