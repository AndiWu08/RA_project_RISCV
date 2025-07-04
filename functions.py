# initialize instruction count to 0
ic = 0
labels = {}

def execute_opcode(opcode, operands, regs, ram):
    global ic
    ## Immediate Instructions
    if opcode == "ADDI":
        dest, reg1, val = operands
        result = regs.regs[int(reg1)] + int(val)

        regs[int(dest)] = result

    elif opcode == "ANDI":
        dest, reg1, val = operands
        result = regs[int(reg1)] & int(val)

        regs[int(dest)] = result

    elif opcode == "ORI":
        dest, reg1, val = operands
        result = regs[int(reg1)] | int(val)

        regs[int(dest)] = result


    ## arithmetic instructions
    elif opcode == "ADD":
        dest, reg1, reg2 = operands
        result = regs[int(reg1)] + regs[int(reg2)]

        regs[int(dest)] = result
    
    elif opcode == "SUB":
        dest, reg1, reg2 = operands
        result = regs[int(reg1)] - regs[int(reg2)]

        regs[int(dest)] = result


    ## logical instructions
    elif opcode == "AND":
        dest, reg1, reg2 = operands
        result = regs[int(reg1)] & regs[int(reg2)]

        regs[int(dest)] = result

    elif opcode == "OR":
        dest, reg1, reg2 = operands
        result = regs[int(reg1)] | regs[int(reg2)]

        regs[int(dest)] = result

    elif opcode == "XOR":
        dest, reg1, reg2 = operands
        result = regs[int(reg1)] ^ regs[int(reg2)]

        regs[int(dest)] = result
    
    # shift left logical immmediate
    elif opcode == "SLLI":
        dest, reg1, shift = operands

        reg1_val = regs[int(reg1)]
        # shift value in reg1 and enforce 32 bit
        result = reg1_val << int(shift) & 0xFFFFFFFF

        regs[int(dest)] = result

    # set less than
    elif opcode == "SLT":
        dest, reg1, reg2 = operands

        if regs[int(reg1)] < regs[int(reg2)]:
            regs[int(dest)] = 1
        else:
            regs[int(dest)] = 0
    

    ## memory access
    elif opcode == "SW":
        reg_value, offset, reg_address = operands

        address = regs[int(reg_address)] + int(offset)
        store_value = regs[int(reg_value)]

        ram.write_word(address, store_value)

    elif opcode == "LW":
        dest, offset, reg_address = operands

        address = regs[int(reg_address)] + int(offset)
        value = ram.read_word(address)

        regs[int(dest)] = value

    
    ## branching 
    elif opcode == "BEQ":
        reg1, reg2, target = operands

        if regs[int(reg1)] == regs[int(reg2)]:
            if target in labels:
                ic = labels[target]
                return True

    elif opcode == "BNE":
        reg1, reg2, target = operands

        if regs[int(reg1)] != regs[int(reg2)]:
            if target in labels:
                ic = labels[target]
                return True
    
    # jumps
    elif opcode == "J":
        target = operands[0]
        
        if target in labels:
            ic = labels[target]
            return True
        
    elif opcode == "JAL":
        reg_return, target = operands

        # save return address (one line after current)
        regs[int(reg_return)] = ic + 1

        # set ic to label position 
        if target in labels:
            ic = labels[target]
            return True
        
    elif opcode == "JALR":
        reg_return, offset, reg_target = operands

        # save return address
        regs[int(reg_return)] = ic + 1

        ic = regs[int(reg_target)] + int(offset)
        return True


# get opcode and operands of current line
def clean_line(line):
    # get opcode
        opcode = line[0]

        # get operands, if there are any
        # remove any characters that aren't necessary later
        operands = []
        if len(line) > 1:
            operands = [
                            cleaned
                            for op in line[1:]
                            if (cleaned := op.replace(',', '')
                                            .replace('(', ' ')
                                            .replace(')', ' ')
                                            .replace('X', '')
                                            .strip())
                        ]
        return opcode, operands 


# file gets parsed to list of instructions
# labels are saved in dictionary
# returns [instructions]
def read_file(file):
    instructions = []
    with open(file, 'r') as f:
        line_count = 0
        for line in f:
            # get rid of parentheses to ensure proper handling in clean_line
            line = line.replace('(', ' ').replace(')', ' ')
            line = ' '.join(line.split())
            line = line.strip()

            # look for labels and save position in dictionary
            if ':' in line:
                label = line.split(':')[0].strip()
                labels[label.upper()] = line_count

            # parse line into instructions
            instructions.append(line)
            line_count += 1
    return instructions


# exexutes list of instructions
def run_asm(instructions, regs, ram, debug=False):
    global ic
    global labels
    ic = 0

    # execute assembler code
    while ic < len(instructions):
        # read line of current instruction count
        # upper -> no case sensitivity
        # split -> get tokens divided by ' '
        line = instructions[ic].upper().split()

        # skip empty lines and label declarations
        if not line or ':' in line:
            ic +=1 
            continue

        opcode, operands = clean_line(line)
        
        ic_modified = execute_opcode(opcode, operands, regs, ram)

        if not ic_modified:
            ic +=1

        # check debug
        if debug:
            print(f"current line: {line}")
            print(f"opcode: {opcode}, operands: {operands}")
            print(f"labels: {labels}")
            print(f"(next) instruction count: {ic}")
            print(regs)

            if input("enter X to break, any other to continue: ").strip().upper() == 'X':
                break
    
    # reset labels
    labels =  {}