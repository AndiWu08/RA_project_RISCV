class RegisterRISC:
    def __init__(self):
      # initialize with 32 empty registers
      self.regs = [0] * 32

    def __setitem__(self, idx, value):
       # update register,
       # x0 has to stay 0
       if idx != 0:
          self.regs[idx] = value

    def __getitem__(self, idx):
       return self.regs[idx]

    def __str__(self):
        output = "--- CURRENT REGISTER CONTENTS ---\n"
        for i in range(len(self.regs)):
           output += f"x{i:02}: {self.regs[i]}\t \t"
           if (i + 1) % 4 == 0:
               output += "\n"
        
        return output
         
class RAM:
    def __init__(self, size_kb=1024):
        # 1MB RAM default
        self.size = size_kb * 1024
        self.memory = bytearray(self.size) 
    
    def read_byte(self, address):
        #check if address is in existing range
        if 0 <= address < self.size:
            return self.memory[address]

    
    def write_byte(self, address, value):
        #check if address is in existing range
        if 0 <= address < self.size:
            self.memory[address] = value & 0xFF

    # functions for lw and sw
    def read_word(self, address):
        # read in 8-bit intervalls
        return (self.read_byte(address) |
               (self.read_byte(address+1) << 8) |
               (self.read_byte(address+2) << 16) |
               (self.read_byte(address+3) << 24))
    
    def write_word(self, address, value):
        # ensure word is 32 bits, force 32-bit
        value = value & 0xFFFFFFFF

        # write in 8-bit intervalls
        self.write_byte(address, value & 0xFF)
        self.write_byte(address+1, (value >> 8) & 0xFF)
        self.write_byte(address+2, (value >> 16) & 0xFF)
        self.write_byte(address+3, (value >> 24) & 0xFF)
    
    def memory_dump(self, start_addr, end_addr):
        print(f"Memory dump [0x{start_addr:08x}-0x{end_addr:08x}]:")
        for addr in range(start_addr, end_addr, 4):
            if addr % 16 == 0:  # New line every 4 words
                print(f"\n0x{addr:08x}: ", end="")
            try:
                word = self.read_word(addr)
                print(f"{word:08x} ", end="")
            except:
                print("-------- ", end="")
        print("\n")