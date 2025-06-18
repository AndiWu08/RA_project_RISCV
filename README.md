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
   - Enter single assembly instruction
   - View memory dump
   - Print register contents
   - Reset registers
   - Reset RAM

### Example Assembly Code

the required example Code (and a few more) can be found in ./test/ and executed using mode 1

note: execute prep08.txt before 08.txt to load an array into RAM

## Project Structure

- `test.py`: Main emulator interface
- `functions.py`: Core instruction execution and file handling
- `regs_and_ram.py`: Register and RAM emulation classes
