"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.address = 0
        self.ram = [0] * 256
        self.registers = [0] * 98
        self.LDI = 0b10000010 # 130
        self.PRN = 0b01000111 # 71
        self.HLT = 0b00000001 # 1


    def ram_read(self, address = None):
        return self.ram[address]
    
    def ram_write(self, value = None, address = None):
        self.ram[address] = value
        return self.ram[address]

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:
            ir = memory[pc]  # Instruction Register, copy of the currently-executing instruction

            if IR == self.LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3

            elif IR == self.PRN:
                print(self.reg[operand_a])
                self.pc += 2

            elif IR == self.HLT:
                running = False
        ​
        #     if ir == 1:  # PRINT_BEEJ
        #         print("Beej!")
        #         pc += 1
        # ​
        #     elif ir == 2:
        #         running = False
        # ​
        #     elif ir == 3:  # SAVE_REG
        #         reg_num = memory[pc + 1]
        #         value = memory[pc + 2]
        #         registers[reg_num] = value
        #         pc += 3
        # ​
        #     elif ir == 4:  # PRINT_REG
        #         reg_num = memory[pc + 1]
        #         print(registers[reg_num])
        #         pc += 2
        # ​
        #     else:
        #         print(f"Unknown instruction {b}")
