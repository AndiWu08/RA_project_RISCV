# Simple RISC-V Emulator

Project for "Rechnerarchitekur": RISCV emulator

## Supported Instructions

- Arithmetic: ADD, ADDI, SUB
- Logical: AND, ANDI, OR, ORI, XOR, SLLI, SLT
- Memory: LW, SW
- Control Flow: BEQ, BNE, J, JAL, JALR

## Usage

1. Run `test.py` to start the emulator
2. Choose from available options:
   - Load assembly code from file
   - Enter single assembly instruction (labels aren't supported in this mode)
   - View memory dump
   - Print register contents
   - Reset registers
   - Reset RAM

### Debug Output Explanation

- **current line**: Line in the instruction list being executed.
- **opcode**: The opcode that will be executed.
- **operands**: Operands used for the current instruction.
- **labels**: All known labels with their corresponding indexes.
- **(next) instruction count**: Instruction counter after execution (not the current line's IC; similar to IT-Systeme).
- **current registers (after execution)**: Register contents after the instruction is executed.

#### Example Debug Output

```
current line: ['ADDI', 'X2,', 'X0,', '2']
opcode: ADDI, operands: ['2', '0', '2']
labels: {'NONSENSE': 3, 'TARGET': 2}
(next) instruction count: 4
--- CURRENT REGISTER CONTENTS ---
x00: 0          x01: 0          x02: 2          x03: 0   
x04: 0          x05: 0          x06: 0          x07: 0   
x08: 0          x09: 0          x10: 0          x11: 0   
x12: 0          x13: 0          x14: 0          x15: 0   
x16: 0          x17: 0          x18: 0          x19: 0   
x20: 0          x21: 0          x22: 0          x23: 0   
x24: 0          x25: 0          x26: 0          x27: 0   
x28: 0          x29: 0          x30: 0          x31: 0 
```

### Example Assembly Code

the required example Code (01.txt - 09.txt) and my own examples can be found in ./test/ and executed using mode 1

note: execute prep08.txt before 08.txt to load an array into RAM

## Project Structure

- `test.py`: Main emulator interface
- `functions.py`: Core instruction execution and file handling
- `regs_and_ram.py`: Register and RAM emulation classes
- `/test`: required example Code and my own examples
