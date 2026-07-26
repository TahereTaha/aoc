
class Computer:
    def __init__(self, reg_a, reg_b, reg_c, program):
        self.__reg_a = reg_a
        self.__reg_b = reg_b
        self.__reg_c = reg_c
        self.__pc = 0
        self.__program = program
        self.__output = []
        self.__halted = False

    def __combo_operand(self, operand):
        if (operand < 4):
            return operand
        if (operand == 4):
            return self.__reg_a
        if (operand == 5):
            return self.__reg_b
        if (operand == 6):
            return self.__reg_c

    #each instruction of the machine.
    def __adv(self, operand):
        self.__reg_a = self.__reg_a // 2 ** self.__combo_operand(operand)
        self.__pc = self.__pc + 2

    def __bxl(self, operand):
        self.__reg_b = self.__reg_b ^ operand
        self.__pc = self.__pc + 2

    def __bst(self, operand):
        self.__reg_b = self.__combo_operand(operand) % 8
        self.__pc = self.__pc + 2

    def __jnz(self, operand):
        if (self.__reg_a != 0):
            self.__pc = operand
        else:
            self.__pc = self.__pc + 2

    def __bxc(self, operand):
        self.__reg_b = self.__reg_b ^ self.__reg_c
        self.__pc = self.__pc + 2
    
    def __out(self, operand):
        self.__output.append(self.__combo_operand(operand) % 8)
        self.__pc = self.__pc + 2

    def __bdv(self, operand):
        self.__reg_b = self.__reg_a // 2 ** self.__combo_operand(operand)
        self.__pc = self.__pc + 2

    def __cdv(self, operand):
        self.__reg_c = self.__reg_a // 2 ** self.__combo_operand(operand)
        self.__pc = self.__pc + 2
    
    def print_machine_state(self):
        print("snapshot of machine state:")
        print("\treg_a:", self.__reg_a)
        print("\treg_b:", self.__reg_b)
        print("\treg_c:", self.__reg_c)
        print("\tpc:", self.__pc)
        print("\tprogram:", self.__program)
        print("\t        ", " " * (3 * self.__pc), "^")
        print("\thalted:", self.__halted)
        print("\toutput:", self.__output)
    
    def step(self):
        if (self.__halted):
            return
        if (self.__program[self.__pc] == 0):
            self.__adv(self.__program[self.__pc + 1])
        elif (self.__program[self.__pc] == 1):
            self.__bxl(self.__program[self.__pc + 1])
        elif (self.__program[self.__pc] == 2):
            self.__bst(self.__program[self.__pc + 1])
        elif (self.__program[self.__pc] == 3):
            self.__jnz(self.__program[self.__pc + 1])
        elif (self.__program[self.__pc] == 4):
            self.__bxc(self.__program[self.__pc + 1])
        elif (self.__program[self.__pc] == 5):
            self.__out(self.__program[self.__pc + 1])
        elif (self.__program[self.__pc] == 6):
            self.__bdv(self.__program[self.__pc + 1])
        elif (self.__program[self.__pc] == 7):
            self.__cdv(self.__program[self.__pc + 1])
        if (self.__pc >= len(self.__program)):
            self.__halted = True
    
    def debug_step(self):
        print("before the step")
        self.print_machine_state();
        print("after the step")
        self.print_machine_state();

    def run(self):
        if (self.__halted):
            return
        while (self.__halted != True):
            self.step()

    def debug_run(self):
        if (self.__halted):
            return
        i = 0
        while (self.__halted != True):
            print("this is the", i, "snapshot")
            self.print_machine_state()
            self.step()
            i = i + 1

    def get_output(self):
        if (self.__halted != True):
            self.run()
        return self.__output





